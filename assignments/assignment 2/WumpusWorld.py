import random


class WumpusWorld:
    def __init__(self, width, height):

        self.agent = {
            "x": 0,
            "y": 0
        }

        self.gold = self.__randspot(width, height)

        while self.gold['x'] == 0 and self.gold['y'] == 0:
            self.gold = self.__randspot(width, height)

        self.wumpus = self.__randspot(width, height)

        while (self.wumpus['x'] == 0 and self.wumpus['y'] == 0) or (
                self.wumpus['x'] == self.gold['y'] and self.wumpus['y'] == self.gold['y']):
            self.gold = self.__randspot(width, height)

        self.board = [[set() for _ in range(width)] for _ in range(height)]

        for row in range(0, height):
            for col in range(0, width):
                pit = True

                if col == self.agent['x'] and row == self.agent['y']:
                    self.board[row][col].add("A")

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
                    if col < width - 1:
                        self.board[row][col + 1].add("B")
                    if row > 0:
                        self.board[row - 1][col].add("B")
                    if row < height - 1:
                        self.board[row + 1][col].add("B")

    def __randspot(self, width, height):
        return {
            "x": random.randint(0, width - 1),
            "y": random.randint(0, height - 1)
        }

    def printBoard(self):
        # TODO: Finish me
        # for row in self.board:
        #     line = ""
        #     for col in row:
        #         add = ""
        #         line = line + "|"
        for row in self.board:
            print(row)

        print("\n\n\n")
        print("W: " + str(self.wumpus))
        print("G: " + str(self.gold))


# Test Case
a = WumpusWorld(5, 6)
a.printBoard()
