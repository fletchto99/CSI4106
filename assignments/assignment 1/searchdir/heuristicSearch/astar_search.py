
from operator import attrgetter
from searchdir.node import *
from searchdir.util import PriorityQueue

## This method must implement A* search
## It must return the solution node and the number of visited nodes
def astar_search(initialState):
	print('A*------------------------------')
	first = Node(initialState)

	# Priority based on the cost of the node
	pq_open = PriorityQueue((lambda x, y: y.f - x.f))

	# Use a set to store the states since we implemented __hash__
	closed = set()
	visited = 0

	pq_open.enqueue(first)

	# Algo as seen in class
	while not pq_open.isEmpty():
		current = pq_open.dequeue()
		visited += 1
		if current.state.isGoal():
			return current, visited
		closed.add(current.state)
		for neighbor in current.expand():
			cost = current.getcost() + neighbor.state.heuristic()
			if cost < neighbor.f:
				# Search for old node since there is no _eq_ fnc in node.py
				# Potentially slow since we need to search through the entire list
				old_node = [node for node in pq_open.show() if node.state == neighbor.state]

				# old_node exists
				if old_node:
					pq_open.show().remove(old_node[0])
				if neighbor.state in closed:
					closed.remove(neighbor.state)
			if neighbor not in pq_open.show() and neighbor not in closed:
				# Queue the neighbours up checking
				pq_open.enqueue(neighbor)
