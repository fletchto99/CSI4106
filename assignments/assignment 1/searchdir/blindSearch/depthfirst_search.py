from searchdir.node import *
from searchdir.util import *

## This method must implement depdth-first search (DFS)
## It must return the solution node and the number of visited nodes
def depthfirst_search(initialState):
    print('DFS------------------------------')
    first = Node(initialState)
    visited = set() # a Set data structure was used for optimized speed
    s = Stack()
    s.push(first) # enqueue the first item

    while not s.isEmpty():
        v = s.pop()
        visited.add(v.state) # add the visited state to the set
        if not v.state.isGoal():
            for newV in v.expand(): # for each new vertice in the list of possible targets.
                if newV.state not in visited :    # if new vertex has not been explored
                    s.push(newV)  # push the new vertice
                    visited.add(newV.state)  # This is not needed, however it does optimize the speed
        else:
            return v, len(visited) #returns the last vertex (solution) and the length of vertex traversed

