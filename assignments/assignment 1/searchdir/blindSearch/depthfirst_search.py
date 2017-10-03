from searchdir.node import *
from searchdir.util import *

## This method must implement depdth-first search (DFS)
## It must return the solution node and the number of visited nodes
def depthfirst_search(initialState):

    visited, s = stack(), [initialState]
    while s:
         vertex = s.pop()
        if vertex not in visited:
             visited.push(vertex)
             s.push(graph[vertex] - visited)
     return visited
