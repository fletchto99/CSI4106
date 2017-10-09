from searchdir.node import *
from searchdir.util import *

## This method must implement depdth-first search (DFS)
## It must return the solution node and the number of visited nodes
def depthfirst_search(initialState):

	v = Node(initialState)
	# visited = {}
	# s = stack()
    visited, s = stack(), [initialState]
    while not s.isEmpty():
    	v = s.pop()
    	if v.state.isGoal():
    		return v, len(visited)
    	else:
            for nextState in v.state.possibleActions(): # for actions
                newVertex = v._createNode(nextState)      # create new vertex from children
                if newVertex.elem not in visited :    # if new node is not visited
                    s.push(newVertex)             # push the newnode
                    visited[newVertex.elem] = newVertex.getcost()       # list up the visited with cost
