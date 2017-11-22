from WumpusWorld import WumpusWorld
from DumbAgent import DumbAgent
from IntellientAgent import IntelligentAgent

print('Running...\n\n')

# The entrypoint for the application
iterations = 10000

# Used for statistics
totalScore = 0
totalDepth = 0
totalTime = 0

for i in range(iterations):
    # Generate a world, where the 0th world is the one from the assignment
    world = WumpusWorld(i)

    # Always ensure the world is solvable
    while not world.solvable():
        world = WumpusWorld(i)

    # Agent without debugging (if debugging is enabled it will print out the map)
    agent = DumbAgent(world, False)

    # Invoke the method to navigate the world
    result = agent.navigate()

    # Statistics to report
    totalScore = totalScore + result['score']
    totalDepth = totalDepth + result['depth']
    totalTime = totalTime + result['time']

print('Dumb Agent:')
print('Total execution time in seconds is: ' + str(totalTime/1000))
print('Final avg score is: ' + str(totalScore/iterations))
print('Final avg depth is: ' + str(totalDepth/iterations))
print('Final avg time in ms is: ' + str(totalTime/iterations))


# Used for statistics
totalScore = 0
totalDepth = 0
totalTime = 0

for i in range(iterations):
    # Generate a world, where the 0th world is the one from the assignment
    world = WumpusWorld(i)

    # Always ensure the world is solvable
    while not world.solvable():
        world = WumpusWorld(i)

    # Agent without debugging (if debugging is enabled it will print out the map)
    agent = IntelligentAgent(world, True)

    # Invoke the method to navigate the world
    # result = agent.navigate()

    # Statistics to report
    totalScore = totalScore + result['score']
    totalDepth = totalDepth + result['depth']
    totalTime = totalTime + result['time']

print('\n\nIntelligent Agent:')
print('Total execution time in seconds is: ' + str(totalTime/1000))
print('Final avg score is: ' + str(totalScore/iterations))
print('Final avg depth is: ' + str(totalDepth/iterations))
print('Final avg time in ms is: ' + str(totalTime/iterations))
