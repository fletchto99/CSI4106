import random
import time
from WumpusWorld import WumpusWorld


class DumbAgent:
    def __init__(self, WumpusWorld, debug):
        self.world = WumpusWorld
        self.fired = False
        self.actions = []
        self.debug = debug

    def navigate(self):
        if self.debug:
            print('Starting world')
            self.world.printBoard()
            print("\n\n\n")

        start = int(round(time.time() * 1000))
        while True:
            justFired = False
            result = ''
            if 'G' in self.world.getLocationProperties():
                self.actions.append('pickup')
                if self.world.pickup():
                    self.actions.append('pickup')
            elif not self.fired and 'S' in self.world.getLocationProperties():
                self.actions.append('fire')
                self.world.fireArrow()
                self.fired = True
                justFired = True
            else:
                rand = random.randint(1, 3)
                if rand == 1:
                    self.actions.append('left')
                    self.world.turnLeft()
                elif rand == 2:
                    self.actions.append('right')
                    self.world.turnRight()
                elif rand == 3:
                    self.actions.append('step')
                    result = self.world.step()

            if not justFired:
                self.fired = False

            if self.debug:
                print("Action Performed: " + str(self.actions[-1]))
                print("World now:")
                self.world.printBoard()
                print("\n\n\n")

            if result == 'dead':
                self.actions.append('dead')
                if self.debug:
                    print('You Died!')
                break

            if self.actions[-1] == 'pickup':
                if self.debug:
                    print('Winner winner chicken dinner')
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
