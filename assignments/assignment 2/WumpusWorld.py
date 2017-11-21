import random


class WumpusWorld:
    def __init__(self):

        self.agent = {
            "x": 0,
            "y": 0
        }

        self.gold = self.__randspot()

        while self.gold['x'] == 0 and self.gold['y'] == 0:
            self.gold = self.__randspot()

        self.wumpus = self.__randspot()

        while self.wumpus['x'] == 0 and self.wumpus['y'] == 0\
                and self.wumpus['x'] == self.gold['y'] and self.wumpus['y'] == self.gold['y']:
            self.gold = self.__randspot()

        self.board = [[set() for _ in range(4)] for _ in range(4)]

        for row in range(0, 4):
            for col in range(0, 4):
                pit = True

                if col == self.agent['x'] and row == self.agent['y']:
                    self.board[row][col].add("A")
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

                if pit and random.uniform(0, 1) < 0.2:
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
            "x": random.randint(0, 4 - 1),
            "y": random.randint(0, 4 - 1)
        }

    def printBoard(self):
        count = 0
        print("============================================")
        for row in self.board:
            print("|| ", end='')
            for col in row:
                if(len(list(col)) == 0):
                    print("         |", end='')
                elif(len(list(col)) == 1):
                    print("    " + str(list(col).__str__().replace('{','').replace('}','').replace('[','').replace(']','').replace(',','').replace("'",'')) + "    |", end='')
                elif(len(list(col)) == 2):
                    print("   " + str(list(col).__str__().replace('{','').replace('}','').replace('[','').replace(']','').replace(',','').replace("'",'')) + "   |", end='')
                elif(len(list(col)) == 3):
                    print("  " + str(list(col).__str__().replace('{','').replace('}','').replace('[','').replace(']','').replace(',','').replace("'",'')) + "  |", end='')
                else:
                    print(" " + str(list(col).__str__().replace('{','').replace('}','').replace('[','').replace(']','').replace(',','').replace("'",'')) + " |", end='')

            if (count == 3):
                print("|\n============================================")
            else:
                print("|\n--------------------------------------------")
            count = count + 1
        print("\n\n\n")
        for row in self.board:
            print(row)

        print("\n\n\n")
        print("W: " + str(self.wumpus))
        print("G: " + str(self.gold))


# Test Case
a = WumpusWorld()
a.printBoard()
