import time
import functools

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

            # Find the percepts for the current location
            perceptions = self.world.getLocationProperties()

            # Add the percepts to a knowledge base using AIMA open source libraries (as recommended in the assignment)
            # Only add the percepts if we haven't visited this grid location yet
            if self.board[location['y']][location['x']][1] == '':
                for perception in perceptions:
                    # Build a propositional knowledge database with the information we have about this tile
                    self.kb.tell('{}{}{}'.format(str(perception), location['x'], location['y']))

                # Check the knowledge base if the current tile is safe using propositional logic
                res = 'u' if self.kb.ask('B{}{}^S{}{}'.format(location['x'], location['y'],location['x'], location['y'])) else 's'

                # Mark the current grid location as visited and tell the user if it + the squares around it are safe
                self.board[location['y']][location['x']][0] = True
                self.board[location['y']][location['x']][1] = res

                # If our current tile is safe then we know that we can at least travel to tiles in all directions
                # surrounding this tile, since they too will be safe
                if res == 's':
                    if location['x'] > 0 and self.board[location['y']][location['x'] - 1][1] == '':
                        self.board[location['y']][location['x'] - 1][1] = 's'
                    if location['x'] < 3 and self.board[location['y']][location['x'] + 1][1] == '':
                        self.board[location['y']][location['x'] + 1][1] = 's'
                    if location['y'] > 0 and self.board[location['y'] - 1][location['x']][1] == '':
                        self.board[location['y'] - 1][location['x'] - 1][1] = 's'
                    if location['y'] < 3 and self.board[location['y'] + 1][location['x']][1] == '':
                        self.board[location['y'] + 1][location['x']][1] = 's'

            # Find possible tiles to traverse to
            grid_as_tuple = (location['x'], location['y'])
            safe_tiles = []
            for row in range(0,4):
                for col in range(0, 4):
                    if self.board[row][col][1] == 's' and not self.board[row][col][0]:
                        safe_tiles.append((row, col))

            # Find closest, unvisited, safe tile
            safe_tiles.sort(key=functools.cmp_to_key(lambda a, b: self.__heuristic(a, grid_as_tuple) - self.__heuristic(b, grid_as_tuple)))

            # Find the shortest path to the nearest known safe tile
            path = self.astart_closest(grid_as_tuple, safe_tiles[0])

            # First check for the gold, if we've found it then pick it up
            if 'G' in perceptions:
                # Attempt to pickup the gold
                if self.world.pickup():
                    self.actions.append('pickup')

            # Attempt to fire the bow if we detect a stench and we didn't just fire the bow
            elif len(path) == 0:
                # TODO: Uh oh, we need to traverse to a tile which could potentially be unsafe..
                # TODO: Travel to the nearest stench and fire an arrow in the direction of another stench
                # TODO: Update the KB stating that the wumpus was likely killed
                # TODO: if the arrow has been fired, then travel to the nearest unsafe tile
                stenches = self.kb.ask("s")
                pass
            else:
                # TODO: Traverse the path of known safe tiles
                pass

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
    def __expand(self, coord, board):
        values = []

        if coord[0] > 0 and 's' == board[coord[1]][coord[0] - 1]:
            values.append((coord[0] - 1, coord[1]))
        if coord[0] < 3 and 's' == board[coord[1]][coord[0] + 1]:
            values.append((coord[0] + 1, coord[1]))
        if coord[1] > 0 and 's' == board[coord[1] - 1][coord[0]]:
            values.append((coord[0], coord[1] - 1))
        if coord[1] < 3 and 's' == board[coord[1] + 1][coord[0]]:
            values.append((coord[0], coord[1] + 1))
        return values

    def astart_closest(self, startState, board, endState):

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
            for child in self.__expand(current_node[1], board):
                if child not in closed:
                    pq_open.enqueue((self.__heuristic(startState, endState), child, current_node))

        return []