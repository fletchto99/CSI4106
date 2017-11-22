import random
import time


# The dumb agent based off of the criteria from the assignment
class DumbAgent:

    def __init__(self, WumpusWorld, debug):
        self.world = WumpusWorld
        self.fired = False
        self.actions = []
        self.debug = debug

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
            justFired = False
            result = ''

            # Check if we found the gold, if so apply the pickup action
            if 'G' in self.world.getLocationProperties():
                # Attempt to pickup the gold
                if self.world.pickup():
                    self.actions.append('pickup')
            # Attempt to fire the bow if we detect a stench and we didn't just fire the bow
            elif not self.fired and 'S' in self.world.getLocationProperties():
                self.world.fireArrow()
                self.actions.append('fire')

                # Track if we fired the arrow
                self.fired = True
                justFired = True
            else:
                # Randomly apply one of the three remaining actions
                rand = random.randint(1, 3)
                if rand == 1:
                    self.world.turnLeft()
                    self.actions.append('left')
                elif rand == 2:
                    self.world.turnRight()
                    self.actions.append('right')
                elif rand == 3:
                    # The result of stepping is tracked, in case we die or walk into a wall
                    result = self.world.step()
                    self.actions.append('step')

            # Checks if the user didn't just fire their arrow and if so reset the fired status
            if not justFired and self.fired:
                self.fired = False

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
            # The depth is -1 because the last action is not an action but rather the result
            "depth": len(self.actions)-1,
            "time": int(round(time.time() * 1000)) - start,
            "optimal": False,
            "complete": False
        }
