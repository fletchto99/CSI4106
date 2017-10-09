from searchdir.node import *
from searchdir.util import *

## This method must implement Breadth-first search (BFS)
## It must return the solution node and the number of visited nodes
def breadthfirst_search(initialState):
    print('BFS------------------------------')
    first = Node(initialState)
    visited = []
    q = Queue()
    q.enqueue(first)

    while not q.isEmpty():
        v = q.dequeue()  # dequeue the vertex (or node)
        visited.append(v)
        if not v.state.isGoal():
            for _next in v.expand():
                if _next not in visited:
                    q.enqueue(_next)
        else:
        	return v, len(visited) # return solution



