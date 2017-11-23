import time

from aima.logic import *
from PriorityQueue import *


# The intelligent agent based off of propositional logic
class IntelligentAgent:
    def __init__(self, WumpusWorld, debug):
        self.world = WumpusWorld
        self.fired = False
        self.actions = []
        self.debug = debug
        self.kb = PropKB()
        self.board = [[[False, ''] for _ in range(4)] for _ in range(4)]

    # Navigates through the world, returning some statistics about its journey
    def navigate(self):

        # Print out the starting world if debug mode is enabled
        if self.debug:
            print('Starting world')
            self.world.printBoard()
            print("\n\n\n")

        # Compute the start time
        start = int(round(time.time() * 1000))

        # Loop until we either die or find the gold
        while True:
            # local vars for tracking
            result = ''
            location = self.world.getAgentLocation()

            # Check if we found the gold, if so apply the pickup action
            if 'G' in self.world.getLocationProperties():
                # Attempt to pickup the gold
                if self.world.pickup():
                    self.actions.append('pickup')

            # Find the percepts for the current location
            perceptions = self.world.getLocationProperties()

            grid = self.board[location['y']][location['x']]

            # Add the percepts to a knowledge base using AIMA open source libraries (as recommended in the assignment)
            # Only add the percepts if we haven't visited this grid location yet
            if grid[1] == '':
                for perception in perceptions:
                    self.kb.tell('{}{}{}'.format(str(perception), location['x'], location['y']))

                res = 'u' if self.kb.ask('B{}{}^S{}{}'.format(location['x'], location['y'],location['x'], location['y'])) else 's'

                # Mark the current grid location as visited and tell the user if it + the squares around it are safe
                self.board[location['y']][location['x']][0] = True
                self.board[location['y']][location['x']][1] = res

                if res == 's':
                    if location['x'] > 0 and self.board[location['y']][location['x'] - 1][1] == '':
                        self.board[location['y']][location['x'] - 1][1] = 's'
                    if location['x'] < 3 and self.board[location['y']][location['x'] + 1][1] == '':
                        self.board[location['y']][location['x'] + 1][1] = 's'
                    if location['y'] > 0 and self.board[location['y'] - 1][location['x']][1] == '':
                        self.board[location['y'] - 1][location['x'] - 1][1] = 's'
                    if location['y'] < 3 and self.board[location['y'] + 1][location['x']][1] == '':
                        self.board[location['y'] + 1][location['x']][1] = 's'





            # Check if we found the gold, if so apply the pickup action
            if 'G' in perceptions:
                # Attempt to pickup the gold
                if self.world.pickup():
                    self.actions.append('pickup')

            # Attempt to fire the bow if we detect a stench and we didn't just fire the bow
            else:

                if location['x'] == unsafePath['x'] and location['y'] == unsafePath['y']:
                    # Turn around if we're heading on an unsafe path to bo back to a known safe ares
                    # the goal is to map out all safe areas before exploring unknone areas (i.e. find
                    # the wumpus an kill it)
                    self.world.turnRight()
                    self.actions.append('right')
                    self.world.turnRight()
                    self.actions.append('right')
                    self.world.step()
                    self.actions.append('step')

            if self.debug:
                # prints out some details about the current run
                print("Action Performed: " + str(self.actions[-1]))
                if str(self.actions[-1]) and result == 'bump':
                    print('You bumped into the wall')
                print("World now:")
                self.world.printBoard()
                print("\n\n\n")

            # Checks if the user has died, if so stop looping
            if result == 'dead':
                self.actions.append('dead')
                if self.debug:
                    print('You Died!')
                break

            # Checks if the user has found the gold, if so stop looping
            if self.actions[-1] == 'pickup':
                if self.debug:
                    print('The gold has been found!')
                break

        # Tidy the output for the next map
        if self.debug:
            print("\n\n")

        # Compute the score of the journey
        score = 0
        for action in self.actions:
            if action == 'pickup':
                score = score + 1000
            elif action == 'dead':
                score = score - 1000
            elif action == 'fire':
                score = score - 10
            else:
                score = score - 1

        # Return some statistics which will be required for the report
        return {
            "score": score,
            "depth": len(self.actions) - 1,
            "time": int(round(time.time() * 1000)) - start,
            "optimal": False,
            "complete": False
        }

    # Manhattan distance from one position to another
    def __heuristic(self, coord1, coord2):
        return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

    # Expand the frontier to only nodes which don't contain pits. All other tiles are valid to traverse to
    def __expand(self, coord):
        values = []

        if coord[0] > 0 and 'P' not in self.board[coord[1]][coord[0] - 1]:
            values.append((coord[0] - 1, coord[1]))
        if coord[0] < 3 and 'P' not in self.board[coord[1]][coord[0] + 1]:
            values.append((coord[0] + 1, coord[1]))
        if coord[1] > 0 and 'P' not in self.board[coord[1] - 1][coord[0]]:
            values.append((coord[0], coord[1] - 1))
        if coord[1] < 3 and 'P' not in self.board[coord[1] + 1][coord[0]]:
            values.append((coord[0], coord[1] + 1))
        return values

    def astart_closest(self, startState, endState):

        pq_open = PriorityQueue((lambda x, y: y[0] - x[0]))
        pq_open.enqueue((self.__heuristic(startState, endState), startState, None))
        closed = set()

        while not pq_open.isEmpty():
            current_node = pq_open.dequeue()
            if current_node[1] == endState:
                path = []
                while current_node is not None:
                    path.append(current_node[2])
                    current_node = current_node[2]
                path.reverse()
                return path

            closed.add(current_node[1])
            for child in self.__expand(current_node[1]):
                if child not in closed:
                    pq_open.enqueue((self.__heuristic(startState, endState), child, current_node))

        return []