import random

from PriorityQueue import PriorityQueue


class WumpusWorld:

    def __init__(self, simulationNumber):

        self.agent = {
            "x": 0,
            "y": 3,
            "heading": ">",
            "arrows": 1
        }

        if simulationNumber == 0:
            self.gold ={
                "x": 1,
                "y": 1
            }
        else:
            self.gold = self.__randspot()

        while self.gold['x'] == 0 and self.gold['y'] == 3:
            self.gold = self.__randspot()

        if simulationNumber == 0:
            self.wumpus ={
                "x": 0,
                "y": 1
            }
        else:
            self.wumpus = self.__randspot()

        while (self.wumpus['x'] == 0 and self.wumpus['y'] == 3) \
                or (self.wumpus['x'] == self.gold['x'] and self.wumpus['y'] == self.gold['y']):
            self.wumpus = self.__randspot()

        self.board = [[set() for _ in range(4)] for _ in range(4)]
        self.pits = []

        for row in range(0, 4):
            for col in range(0, 4):
                pit = True

                if col == self.agent['x'] and row == self.agent['y']:
                    pit = False

                if col == self.gold['x'] and row == self.gold['y']:
                    self.board[row][col].add("G")
                    pit = False

                if col == self.wumpus['x'] and row == self.wumpus['y']:
                    self.board[row][col].add("W")
                    pit = False

                if row == self.wumpus['y'] and (col == self.wumpus['x'] - 1 or col == self.wumpus['x'] + 1):
                    self.board[row][col].add("S")
                elif col == self.wumpus['x'] and (row == self.wumpus['y'] - 1 or row == self.wumpus['y'] + 1):
                    self.board[row][col].add("S")

                check = simulationNumber == 0 and ((row == 0 and col ==3) or (row == 1 and col == 2) or (row == 3 and col == 2))

                if check or (simulationNumber != 0 and pit and random.uniform(0, 1) < 0.2):
                    self.pits.append({
                        "x": col,
                        "y": row
                    })
                    self.board[row][col].add("P")
                    if col > 0:
                        self.board[row][col - 1].add("B")
                    if col < 4 - 1:
                        self.board[row][col + 1].add("B")
                    if row > 0:
                        self.board[row - 1][col].add("B")
                    if row < 4 - 1:
                        self.board[row + 1][col].add("B")

    def __randspot(self):
        return {
            "x": random.randint(0, 3),
            "y": random.randint(0, 3)
        }

    def printBoard(self):
        count = 0
        rcount = 4
        print("  ============================================")
        for i in range(0, 4):
            print(str(rcount) + " || ", end='')
            for j in range(0, 4):

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

    def fireArrow(self):
        if self.agent['arrows'] == 0:
            return False

        self.agent['arrows'] = self.agent['arrows'] -1
        killed = False
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

        if killed:
            for row in range(4):
                for col in range(4):
                    if "S" in self.board[row][col]:
                        self.board[row][col].remove("S")
                    if "W" in self.board[row][col]:
                        self.board[row][col].remove("W")
            return True
        return False

    def turnRight(self):
        for i in range(3):
            self.turnLeft()

    def turnLeft(self):
        if self.agent['heading'] == "^":
            self.agent['heading'] = "<"
        elif self.agent['heading'] == "<":
            self.agent['heading'] = "v"
        elif self.agent['heading'] == "v":
            self.agent['heading'] = ">"
        elif self.agent['heading'] == ">":
            self.agent['heading'] = "^"

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

        if (self.agent['x'] == self.wumpus['x'] and self.agent['y'] == self.wumpus['y']) \
                or {"x": self.agent['x'], "y": self.agent['y']} in self.pits:
            return 'dead'
        return 'success'

    def pickup(self):
        if self.agent['x'] == self.gold['x'] and self.agent['y'] == self.gold['y']:
            return True
        return False

    def getLocationProperties(self):
        return self.board[self.agent['y']][self.agent['x']]

    def getAgentLocation(self):
        return self.agent

    def __heuristic(self, coord1, coord2):
        return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

    # Expand the frontier to only nodes which don't contain pits
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

    def solvable(self):

        agent = (self.agent['x'], self.agent['y'])
        gold = (self.gold['x'], self.gold['y'])

        open_nodes = PriorityQueue((lambda x, y: y[0] - x[0]))
        open_nodes.enqueue((self.__heuristic(agent, gold), agent, None))
        closed = set()

        while not open_nodes.isEmpty():
            current_node = open_nodes.dequeue()
            if current_node[1] == gold:
                while current_node is not None:
                    current_node = current_node[2]
                return True

            closed.add(current_node[1])
            for child in self.__expand(current_node[1]):
                if child not in closed:
                    open_nodes.enqueue((self.__heuristic(child, gold), child, current_node))

        return False