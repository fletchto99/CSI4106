from WumpusWorld import WumpusWorld
from DumbAgent import DumbAgent

total = 0
iterations = 100000
for i in range(iterations):
    world = WumpusWorld()
    agent = DumbAgent(world, False)
    total = total + agent.play()['score']

print('final score is: ' + str(total/iterations))
