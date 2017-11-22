import random

from PriorityQueue import PriorityQueue


# The wumpus world according to the specifications of the assignment
class WumpusWorld:
    def __init__(self, simulationNumber):

        # Our agent spawns at the bottom left heading east
        self.agent = {
            "x": 0,
            "y": 3,
            "heading": ">",
            "arrows": 1
        }

        # If we're using the simulation from the assignment and not a random one
        # then we place the gold at a specific location
        if simulationNumber == 0:
            self.gold = {
                "x": 1,
                "y": 1
            }
        else:
            # otherwise we place the gold randomly
            self.gold = self.__randspot()

        # Determine if the gold is in a valid location, that is
        # that the gold is not under the agent to begin with
        while self.gold['x'] == 0 and self.gold['y'] == 3:
            self.gold = self.__randspot()

        # We now spawn the wumpus into the world, again using the location
        # provided by the assignment for simulation 0
        if simulationNumber == 0:
            self.wumpus = {
                "x": 0,
                "y": 1
            }
        else:
            # Otherwise we place the wumpus randomly on the map
            self.wumpus = self.__randspot()

        # We need to ensure the wumpus doesn't spawn on the agent or the gold
        while (self.wumpus['x'] == 0 and self.wumpus['y'] == 3) \
                or (self.wumpus['x'] == self.gold['x'] and self.wumpus['y'] == self.gold['y']):
            self.wumpus = self.__randspot()

        # Build out an empty board to begin with
        self.board = [[set() for _ in range(4)] for _ in range(4)]
        self.pits = []

        # Populate the board with the pits, breezes, agent, wumpus and stenches
        for row in range(0, 4):
            for col in range(0, 4):
                # Used to track if the current square is a valid location for the pit
                pit = True

                # Place the agent if the location is right
                if col == self.agent['x'] and row == self.agent['y']:
                    pit = False

                # Place the gold, if the location is right
                if col == self.gold['x'] and row == self.gold['y']:
                    self.board[row][col].add("G")
                    pit = False

                # Place the wumpus if the location is right
                if col == self.wumpus['x'] and row == self.wumpus['y']:
                    self.board[row][col].add("W")
                    pit = False

                # Place the stench tiles around the wumpus
                if row == self.wumpus['y'] and (col == self.wumpus['x'] - 1 or col == self.wumpus['x'] + 1):
                    self.board[row][col].add("S")
                elif col == self.wumpus['x'] and (row == self.wumpus['y'] - 1 or row == self.wumpus['y'] + 1):
                    self.board[row][col].add("S")

                # A check to populate the pits in simulation 0, otherwise randomness will be used
                check = simulationNumber == 0 \
                        and ((row == 0 and col == 3) or (row == 1 and col == 2) or (row == 3 and col == 2))

                # Place pits according to a 20% chance, unless we're in simulation 0
                if check or (simulationNumber != 0 and pit and random.uniform(0, 1) < 0.2):
                    self.pits.append({
                        "x": col,
                        "y": row
                    })
                    self.board[row][col].add("P")

                    # Create the breezes around the pit
                    if col > 0:
                        self.board[row][col - 1].add("B")
                    if col < 4 - 1:
                        self.board[row][col + 1].add("B")
                    if row > 0:
                        self.board[row - 1][col].add("B")
                    if row < 4 - 1:
                        self.board[row + 1][col].add("B")

    # A helper method to generate a random tile on the board
    def __randspot(self):
        return {
            "x": random.randint(0, 3),
            "y": random.randint(0, 3)
        }

    # Prints the entire map out in a clean manner
    def printBoard(self):
        count = 0
        rcount = 4
        print("  ============================================")
        for i in range(0, 4):
            print(str(rcount) + " || ", end='')
            for j in range(0, 4):

                # Convert to a temp list so we can add the agent if its on this square
                props = list(self.board[i][j])

                if self.agent['y'] == i and self.agent['x'] == j:
                    props.append(self.agent['heading'])

                if len(props) == 0:
                    print("         |", end='')
                elif len(props) == 1:
                    print("    " + str(
                        props.__str__().replace('{', '').replace('}', '').replace('[', '').replace(']', '').replace(
                            ',', '').replace("'", '')) + "    |", end='')
                elif len(props) == 2:
                    print("   " + str(
                        props.__str__().replace('{', '').replace('}', '').replace('[', '').replace(']', '').replace(
                            ',', '').replace("'", '')) + "   |", end='')
                elif len(props) == 3:
                    print("  " + str(
                        props.__str__().replace('{', '').replace('}', '').replace('[', '').replace(']', '').replace(
                            ',', '').replace("'", '')) + "  |", end='')
                else:
                    print(" " + str(
                        props.__str__().replace('{', '').replace('}', '').replace('[', '').replace(']', '').replace(
                            ',', '').replace("'", '')) + " |", end='')

            if (count == 3):
                print("|\n  ============================================")
                print("         1         2         3         4")
            else:
                print("|\n  --------------------------------------------")
            rcount = rcount - 1
            count = count + 1

    # Fires an arrow from the current position to the nearest wall in the heading we're facing
    def fireArrow(self):

        # No arrows left
        if self.agent['arrows'] == 0:
            return False

        # Subtract an arrow once we fire
        self.agent['arrows'] = self.agent['arrows'] - 1
        killed = False

        # Fire the arrow in the heading, and check if the wumpus was killed
        if self.agent['heading'] == ">":
            for i in range(self.agent['x'], 4):
                if self.agent['y'] == self.wumpus['y'] and i == self.wumpus['x']:
                    killed = True
        elif self.agent['heading'] == "<":
            for i in range(0, self.agent['x']):
                if self.agent['y'] == self.wumpus['y'] and i == self.wumpus['x']:
                    killed = True
        elif self.agent['heading'] == "v":
            for i in range(self.agent['y'], 4):
                if self.agent['x'] == self.wumpus['x'] and i == self.wumpus['y']:
                    killed = True
        elif self.agent['heading'] == "^":
            for i in range(0, self.agent['y']):
                if self.agent['x'] == self.wumpus['x'] and i == self.wumpus['y']:
                    killed = True

        # If the wumpus was killed, remove it from the board
        if killed:
            for row in range(4):
                for col in range(4):
                    if "S" in self.board[row][col]:
                        self.board[row][col].remove("S")
                    if "W" in self.board[row][col]:
                        self.board[row][col].remove("W")
            return True
        return False

    # Changes the heading to the right
    def turnRight(self):
        for i in range(3):
            self.turnLeft()

    # Changes the heading to the left
    def turnLeft(self):
        if self.agent['heading'] == "^":
            self.agent['heading'] = "<"
        elif self.agent['heading'] == "<":
            self.agent['heading'] = "v"
        elif self.agent['heading'] == "v":
            self.agent['heading'] = ">"
        elif self.agent['heading'] == ">":
            self.agent['heading'] = "^"

    # Steps in the direction we're facing, checking if we bump into a wall
    # If we fall into a pit or run into the wumpus we die
    def step(self):
        if self.agent['heading'] == "^":
            if self.agent['y'] == 0:
                return 'bump'
            self.agent['y'] = self.agent['y'] - 1
        elif self.agent['heading'] == "<":
            if self.agent['x'] == 0:
                return 'bump'
            self.agent['x'] = self.agent['x'] - 1
        elif self.agent['heading'] == "v":
            if self.agent['y'] == 3:
                return 'bump'
            self.agent['y'] = self.agent['y'] + 1
        elif self.agent['heading'] == ">":
            if self.agent['x'] == 3:
                return 'bump'
            self.agent['x'] = self.agent['x'] + 1

        # Check for death
        if (self.agent['x'] == self.wumpus['x'] and self.agent['y'] == self.wumpus['y']) \
                or {"x": self.agent['x'], "y": self.agent['y']} in self.pits:
            return 'dead'
        return 'success'

    # Attempts to pickup the gold, returning true if the gold is on the same square
    def pickup(self):
        if self.agent['x'] == self.gold['x'] and self.agent['y'] == self.gold['y']:
            return True
        return False

    # Returns a list of the percepts at the current location of the agent
    def getLocationProperties(self):
        return self.board[self.agent['y']][self.agent['x']]

    # Returns the location of the agent as a dict
    def getAgentLocation(self):
        return self.agent

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

    # A* As seen in assignment 1, slightly modified to work on this board
    def solvable(self):

        agent = (self.agent['x'], self.agent['y'])
        gold = (self.gold['x'], self.gold['y'])

        pq_open = PriorityQueue((lambda x, y: y[0] - x[0]))
        pq_open.enqueue((self.__heuristic(agent, gold), agent, None))
        closed = set()

        while not pq_open.isEmpty():
            current_node = pq_open.dequeue()
            if current_node[1] == gold:
                return True

            closed.add(current_node[1])
            for child in self.__expand(current_node[1]):
                if child not in closed:
                    pq_open.enqueue((self.__heuristic(child, gold), child, current_node))

        return False
