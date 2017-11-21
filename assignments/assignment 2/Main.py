from WumpusWorld import WumpusWorld
from DumbAgent import DumbAgent
from IntellientAgent import IntelligentAgent

print('Dumb Agent\n\n')

iterations = 10000
totalScore = 0
totalDepth = 0
totalTime = 0

for i in range(iterations):
    world = WumpusWorld(iterations)
    # only look at worlds which are solvable
    while not world.solvable():
        world = WumpusWorld(iterations)

    # Agent without debugging (if debugging is enabled it will print out the map)
    agent = DumbAgent(world, False)
    result = agent.navigate()
    totalScore = totalScore + result['score']
    totalDepth = totalDepth + result['depth']
    totalTime = totalTime + result['time']

print('Total execution time in seconds is: ' + str(totalTime/1000))
print('Final avg score is: ' + str(totalScore/iterations))
print('Final avg depth is: ' + str(totalDepth/iterations))
print('Final avg time in ms is: ' + str(totalTime/iterations))


# print('Intelligent Agent\n\n')
#
# iterations = 10
# totalScore = 0
# totalDepth = 0
# totalTime = 0
# for i in range(iterations):
#     world = WumpusWorld(0)
#     agent = IntelligentAgent(world, True)
#     result = agent.navigate()
#     totalScore = totalScore + result['score']
#     totalDepth = totalDepth + result['depth']
#     totalTime = totalTime + result['time']
#
# print('Total execution time in seconds is: ' + str(totalTime/1000))
# print('Final avg score is: ' + str(totalScore/iterations))
# print('Final avg depth is: ' + str(totalDepth/iterations))
# print('Final avg time in ms is: ' + str(totalTime/iterations))
