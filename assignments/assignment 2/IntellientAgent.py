import time

from aima.logic import *


class IntelligentAgent:
    def __init__(self, WumpusWorld, debug):
        self.world = WumpusWorld
        self.fired = False
        self.actions = []
        self.debug = debug
        self.kb = PropKB()

    def navigate(self):
        if self.debug:
            print('Starting world')
            self.world.printBoard()
            print("\n\n\n")

        start = int(round(time.time() * 1000))
        while True:
            # TODO: Implement intelligent agent loop here
            perceptions = self.world.getLocationProperties()
            if 'G' in self.world.getLocationProperties():
                self.actions.append('pickup')
                if self.world.pickup():
                    self.actions.append('pickup')
            for perception in perceptions:
                self.kb.tell({
                    "x": self.world.getAgentLocation()['x'],
                    "y": self.world.getAgentLocation()['y'],
                    "perception": str(perception)
                })
            # if (ask_generator(self, ) :
            #     print(x, y, perception)

            # TODO: Break when the goal state is reached or the person has died
            break

        if self.debug:
            print("\n\n\n")

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
        return {
            "score": score,
            "depth": len(self.actions)-1,
            "time": int(round(time.time() * 1000)) - start,
            "optimal": False,
            "complete": False
        }
