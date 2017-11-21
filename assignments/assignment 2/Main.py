from WumpusWorld import WumpusWorld
from DumbAgent import DumbAgent


iterations = 10
totalScore = 0
totalDepth = 0
totalTime = 0
for i in range(iterations):
    world = WumpusWorld(0)
    agent = DumbAgent(world, True)
    result = agent.play()
    totalScore = totalScore + result['score']
    totalDepth = totalDepth + result['depth']
    totalTime = totalTime + result['time']

print('Total execution time in seconds is: ' + str(totalTime/1000))
print('Final avg score is: ' + str(totalScore/iterations))
print('Final avg depth is: ' + str(totalDepth/iterations))
print('Final avg time in ms is: ' + str(totalTime/iterations))
