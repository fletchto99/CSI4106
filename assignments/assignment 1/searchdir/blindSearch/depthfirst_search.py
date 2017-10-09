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

    while not s.isEmpty():
        v = s.pop()
        visited.append(v)
        if not v.state.isGoal():
            for _next in v.expand():
                if _next not in visited:
                    s.push(_next)
        else:
            return v, len(visited)

