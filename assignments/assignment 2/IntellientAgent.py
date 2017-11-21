import random
import time
from WumpusWorld import WumpusWorld
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
            percepts = self.world.getLocationProperties()
            for percept in percepts:
                self.kb.tell({
                    "x": self.world.getAgentLocation()['x'],
                    "y": self.world.getAgentLocation()['y'],
                    "percept": str(percept)
                })

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
