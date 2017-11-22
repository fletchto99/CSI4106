import time

from aima.logic import *


# The dumb agent based off of propositional logic
class IntelligentAgent:
    def __init__(self, WumpusWorld, debug):
        self.world = WumpusWorld
        self.fired = False
        self.actions = []
        self.debug = debug
        self.kb = PropKB()
        self.locations = []

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
            result = ''

            # Build a visited list
            self.locations.append(self.world.getAgentLocation())

            # Check if we found the gold, if so apply the pickup action
            if 'G' in self.world.getLocationProperties():
                # Attempt to pickup the gold
                if self.world.pickup():
                    self.actions.append('pickup')

            # Find the percepts for the current location
            perceptions = self.world.getLocationProperties()

            # Add the percepts to a knowledge base using AIMA open source libraries (as recommended in the assignment)
            for perception in perceptions:
                self.kb.tell({
                    "x": self.world.getAgentLocation()['x'],
                    "y": self.world.getAgentLocation()['y'],
                    "perception": str(perception)
                })

            # Look for rooms which lead to potentially unsafe rooms
            unsafePath = self.kb.ask({
                "perception": "S^B"
            })

            # Check if we found the gold, if so apply the pickup action
            if 'G' in self.world.getLocationProperties():
                # Attempt to pickup the gold
                if self.world.pickup():
                    self.actions.append('pickup')
            # Attempt to fire the bow if we detect a stench and we didn't just fire the bow
            else:
                loc = self.world.getAgentLocation()

                if loc['x'] == unsafePath['x'] and loc['y'] == unsafePath['y']:
                    # Turn around if we're heading on an unsafe path to bo back to a known safe ares
                    # the goal is to map out all safe areas before exploring unknone areas (i.e. find
                    # the wumpus an kill it)
                    self.world.turnRight()
                    self.actions.append('right')
                    self.world.turnRight()
                    self.actions.append('right')
                    self.world.step()
                    self.actions.append('step')

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
            "depth": len(self.actions) - 1,
            "time": int(round(time.time() * 1000)) - start,
            "optimal": False,
            "complete": False
        }
