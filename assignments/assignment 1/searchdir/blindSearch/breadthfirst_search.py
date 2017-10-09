from searchdir.node import *
from searchdir.util import *

## This method must implement Breadth-first search (BFS)
## It must return the solution node and the number of visited nodes
def breadthfirst_search(initialState):
    print('BFS------------------------------')
    first = Node(initialState)
    visited = {}
    q = Queue()
    q.enqueue(first)
    visited[first.elem] = first.getcost()  # Retreive the cost of the first state

    while not q.isEmpty():
        v = q.dequeue()  # dequeue the vertex (or node)
        if not v.state.isGoal():
            for _next in v.state.possibleActions(): # Find all next possible actions
                newV = v._createNode(_next)      # create a new vertex (or node)
                if newV.elem not in visited :    # if new vertex has not been explored
                    q.enqueue(newV)  # enqueue the new vertice
                    visited[newV.elem] = newV.getcost()   # add the cost to the list

        else:
        	return v, len(visited) # return solution



