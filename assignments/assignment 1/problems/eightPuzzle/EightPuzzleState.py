### Author: Amal Zouaq
### azouaq@uottawa.ca
## Author: Hadi Abdi Ghavidel
## habdi.cnlp@gmail.com

import timeit

import numpy as np
import random
from searchdir.blindSearch.breadthfirst_search import *
from searchdir.blindSearch.depthfirst_search import *
from searchdir.heuristicSearch.astar_search import *
from searchdir.state import *


class EightPuzzleState(State):

    #initializes the eight puzzle with the configuration passed in parameter (numbers)
    def __init__(self, numbers):
        self.state = numbers
        self.boardSize = 3
        if len(self.state) != boardSize**2 or len(self.state) != len(set(self.state)):
            print("Invalid state array!")


    #returns a boolean value that indicates if the current configuration is the same as the goal configuration
    def isGoal(self):
        return self.state == [0, 1, 2, 3, 4, 5, 6, 7, 8]


    # returns the set of legal actions in the current state
    def possibleActions(self):
        possibleactions = []
        #depending on where the blank node is, return the possible actions
        if state.index(0) > self.boardSize:
            possibleactions.append("up")
        if (state.index(0)+1) % self.boardSize != 0:
            possibleactions.append("right")
        if state.index(0) < (self.boardSize**2)-boardSize:
            possibleactions.append("down")
        if state.index(0) % self.boardSize != 0:
            possibleactions.append("left")
        return possibleactions


    # applies the result of the move on the current state
    def executeAction(self, move):
        idx = self.state.index(0)

        # I've created a simple helper function __swap which just swaps the elements
        if move == 'up':
            __swap(idx, idx-self.boardSize)
        elif move == 'right':
            __swap(idx, idx+1)
        elif move == 'down':
            __swap(idx, idx+self.boardSize)
        elif move == 'left':
            __swap(idx, idx-1)

    # A simple helper function to swap the elements
    def __swap(start, end):
        self.state[start], self.state[end] = self.state[end], self.state[start]

    # returns true if the current state is the same as other, false otherwise
    def equals(self, other):
        self.state = other


    # prints the grid representing the current state
    # e.g.
    # -------------
    # |   | 1 | 2 |
    # -------------
    # | 3 | 4 | 5 |
    # -------------
    # | 6 | 7 | 8 |
    # -------------
    def show(self):
        print("-------------", end="\n| ")
        for idx, element in enumerate(self.state):
            print(" " if element == 0 else element, "| ", end = "")
            if (idx+1) % self.boardSize == 0 and idx != 0:
                print("\n-------------", end = "\n" if idx+1 == len(self.state) else "\n| ")


    # returns the cost of the action in parameter
    def cost(self, action):
        return 1 # Will always be 1 in this implementation

    # returns the value of the heuristic for the current state
    # note that you can alternatively call heuristic1() and heuristic2() to test both heuristics with A*
    def heuristic(self):
        return self.heuristic1()
        # return self.heuristic2()


    ## returns the value of your first heuristic for the current state
    # make sure to explain it clearly in your comment
    def heuristic1(self):
        # TO COMPLETE
        pass


    # returns the value of your first heuristic for the current state
    # make sure to explain it clearly in your comment
    def heuristic2(self, matrix, goal):
        # TO COMPLETE
        pass


####################### SOLVABILITY ###########################

def issolvable(puzzle):
    puzzle_str = np.array(list(map(int, puzzle)))
    print("Puzzle string: ", puzzle_str)
    if inversions(puzzle_str) % 2:
        return False
    else : return True

def inversions(s):
    k = s[s != 0]
    return sum(
        len(np.array(np.where(k[i + 1:] < k[i])).reshape(-1))
        for i in range(len(k) - 1)
    )

def randomize(puzzle):
    puzzle = puzzle.shuffle_ran(puzzle, 1)
    puzzle_choice = []
    for sublist in puzzle.cells:
        for item in sublist:
            puzzle_choice.append(item)
    return puzzle, puzzle_choice

    def shuffle_ran(self,board, moves):
        newState = board
        if moves==100:
            return newState
        else:
            newState.executeAction(random.choice(list(board.possibleActions())))
            moves= moves+1
            return self.shuffle_ran(newState, moves)

#######  SEARCH ###########################
EIGHT_PUZZLE_DATA = [[0, 1, 2, 3, 4, 5, 6, 7, 8],
                     [1, 0, 2, 3, 4, 5, 6, 7, 8],
                     [1, 0, 2, 3, 4, 5, 8, 7, 6],
                     [4, 0, 6, 1, 2, 8, 7, 3, 5],
                     [1, 2, 8, 7, 3, 4, 5, 6, 0],
                     [5, 1, 3, 4, 0, 2, 7, 6, 8],
                     [1, 2, 5, 7, 6, 8, 0, 4, 3],
                     [4, 6, 0, 7, 2, 8, 3, 1, 5]]

puzzle_choice = EIGHT_PUZZLE_DATA[6]
puzzle = EightPuzzleState(puzzle_choice)
#puzzle, puzzle_choice = randomize(puzzle)
print('Initial Config')
puzzle.show()
if not issolvable(puzzle_choice):
    print("NOT SOLVABLE")
else:
    start = timeit.default_timer()
    solution, nbvisited = breadthfirst_search(puzzle)
    stop = timeit.default_timer()
    printResults('BFS', solution, start, stop, nbvisited)


    start = timeit.default_timer()
    solution, nbvisited = depthfirst_search(puzzle)
    stop = timeit.default_timer()
    printResults('DFS', solution, start, stop, nbvisited)

    start = timeit.default_timer()
    solution, nbvisited = astar_search(puzzle)
    stop = timeit.default_timer()
    printResults('A*', solution, start, stop, nbvisited)


