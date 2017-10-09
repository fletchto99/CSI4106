
from operator import attrgetter
from searchdir.node import *
from searchdir.util import PriorityQueue

## This method must implement A* search
## It must return the solution node and the number of visited nodes
def astar_search(initialState):
	first = Node(initialState)

	pq_open = PriorityQueue((lambda x, y: x[1] - y[1]))
	closed = []

	pq_open.enqueue((first, first.getcost()))

	while not pq_open.isEmpty():
		current = pq_open.dequeue()[0]
		if current.state.isGoal():
			return len(pq_closed), current.state
		closed.append(current)
		for neighbor in current.expand():
			cost = current.getcost() + neighbor.state.heuristic()
			if neighbor in pq_open.show() and cost < neighbor.getcost():
				pq_open.show().remove(neighbor)
			if neighbor in closed and cost <  neighbor.getcost():
				closed.remove(neighbor)
			if neighbor not in pq_open.show() and neighbor not in closed:
				pq_open.enqueue((neighbor.state, neighbor.getcost()))
