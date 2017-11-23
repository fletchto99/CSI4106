### Author: Amal Zouaq
### azouaq@uottawa.ca
## Author: Hadi Abdi Ghavidel
## habdi.cnlp@gmail.com

import timeit

from searchdir.blindSearch.breadthfirst_search import *
from searchdir.blindSearch.depthfirst_search import *
from searchdir.heuristicSearch.astar_search import *
from searchdir.state import *


class BonusState(State):
    # initializes the eight puzzle with the configuration passed in parameter (numbers)
    def __init__(self, startState):
        self.state = startState

    # returns a boolean value that indicates if the current configuration is the same as the goal configuration
    def isGoal(self):
        # We've reached the goal when every item in the array has the same value as its index
        return self.state == [3, 3, 1]

    def isValid(self, state):
        if state[0] >= 0 and state[1] >= 0 and 3 - state[1] >= 0 and 3 - state[1] >= 0 \
                and (state[0] == 0 or state[0] >= state[1]) and (3 - state[0] == 0 or 3 - state[0] >= 3 - state[1]):
            return True
        else:
            return False

    # returns the set of legal actions in the current state
    def possibleActions(self):

        states = []

        if self.state[2] == 0:
            state = [self.state[0] + 1, self.state[1], 1]
            if self.isValid(state):
                states.append(state)

            state = [self.state[0] + 2, self.state[1], 1]
            if self.isValid(state):
                states.append(state)

            state = [self.state[0], self.state[1] + 1, 1]
            if self.isValid(state):
                states.append(state)

            state = [self.state[0], self.state[1] + 2, 1]
            if self.isValid(state):
                states.append(state)

            state = [self.state[0] + 1, self.state[1] + 1, 1]
            if self.isValid(state):
                states.append(state)

        elif self.state[2] == 1:
            state = [self.state[0] - 1, self.state[1], 0]
            if self.isValid(state):
                states.append(state)

            state = [self.state[0] - 2, self.state[1], 0]
            if self.isValid(state):
                states.append(state)

            state = [self.state[0], self.state[1] - 1, 0]
            if self.isValid(state):
                states.append(state)

            state = [self.state[0], self.state[1] - 2, 0]
            if self.isValid(state):
                states.append(state)

            state = [self.state[0] - 1, self.state[1] - 1, 0]
            if self.isValid(state):
                states.append(state)
        return states

    # applies the result of the move on the current state
    def executeAction(self, move):
        self.state = move  # The possible actions just returns the state

    # returns true if the current state is the same as other, false otherwise
    def equals(self, other):
        return self.state == other

    # Minor optimizations for comparisons used within BFS and A*
    def __eq__(self, other):
        return self.equals(other)

    def __hash__(self):
        return hash(tuple(self.state))

    def show(self):
        print('-----------')
        print('Left side:')
        print('    Missionaries: {}'.format(3 - self.state[0]))
        print('    Cannibals: {}'.format(3 - self.state[1]))
        print('Right side:')
        print('    Missionaries: {}'.format(self.state[0]))
        print('    Cannibals: {}'.format(self.state[1]))
        print('Boat Location: {}'.format('left' if self.state[2] == 0 else 'right'))

    # returns the cost of the action in parameter
    def cost(self, action):
        return 1

    # returns the value of the heuristic for the current state
    # note that you can alternatively call heuristic1() and heuristic2() to test both heuristics with A*
    def heuristic(self):
        # Loads the proper heuristic for the test
        return (3 - self.state[0]) + (3 - self.state[1])


MISSIONARY_DATA = [0, 0, 0]

puzzle = BonusState(MISSIONARY_DATA)
print('Initial Config')
puzzle.show()

start = timeit.default_timer()
solution, nbvisited = breadthfirst_search(puzzle)
stop = timeit.default_timer()
printResults('BFS', solution, start, stop, nbvisited)

start = timeit.default_timer()
solution, nbvisited = astar_search(puzzle)
stop = timeit.default_timer()
printResults('A*', solution, start, stop, nbvisited)
