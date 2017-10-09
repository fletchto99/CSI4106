from searchdir.node import *
from searchdir.util import *

## This method must implement depdth-first search (DFS)
## It must return the solution node and the number of visited nodes
def depthfirst_search(initialState):
    print('DFS------------------------------')
    first = Node(initialState)
    visited = []
    s = Stack()
    s.push(first)
    visited.append(0)

    while not s.isEmpty():
        v = s.pop()
        visited.append(v.getcost())
        if not v.state.isGoal():
            for _next in v.expand():
                if _next.state not in visited:
                    s.push(_next)
                    visited.append(v.getcost())
        else:
            return v, len(visited)

