from searchdir.node import *
from searchdir.util import *


## This method must implement Breadth-first search (BFS)
## It must return the solution node and the number of visited nodes
def breadthfirst_search(initialState):
    print('BFS------------------------------')
    first = Node(initialState)
    visited = set()  # a Set data structure was used for optimized speed
    q = Queue()
    q.enqueue(first)  # enqueue the first item

    while not q.isEmpty():
        v = q.dequeue()
        visited.add(v.state)  # add the visited vertex to the set
        if not v.state.isGoal():
            for newV in v.expand():  # for each new vertice in the list of possible targets.
                if newV.state not in visited:  # if new vertex has not been explored
                    q.enqueue(newV)  # enqueue the new vertice
                    visited.add(newV.state)  # This is not needed, however is does optimize the speed

        else:
            return v, len(visited)  # returns the last vertex (solution) and the length of vertex traversed
