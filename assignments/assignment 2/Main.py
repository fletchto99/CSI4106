from WumpusWorld import WumpusWorld
from DumbAgent import DumbAgent

total = 0
iterations = 10000
for i in range(iterations):
    world = WumpusWorld()
    agent = DumbAgent(world, False)
    total = total + agent.play()['score']

print('The final score is: ' + str(total/iterations))
