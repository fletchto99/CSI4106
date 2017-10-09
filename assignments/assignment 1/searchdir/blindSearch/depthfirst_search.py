from searchdir.node import *
from searchdir.util import *

## This method must implement depdth-first search (DFS)
## It must return the solution node and the number of visited nodes
def depthfirst_search(initialState):
    first = Node(initialState)
    visited = {}
    s = stack()
    s.push(first)
    visited[first.elem] = first.getcost()  # Retreive the cost of the first state

    while not s.isEmpty():
        v = s.pop()
        if not v.state.isGoal():
            for _next in v.state.possibleActions():
                newV = v._createNode(_next)      # create new vertex from children
                if newV.elem not in visited :    # if new node is not visited
                    s.push(newV)             # push the newnode
                    visited[newV.elem] = newV.getcost()       # list up the visited with cost
        else:
            return v, len(visited)

