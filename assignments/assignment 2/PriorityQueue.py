from heapq import heappush, heappop


class PriorityQueue:
    """Implementation of the PriorityQueue data structure."""

    def __init__(self):
        """Initializes the PriorityQueue"""
        self.h = []  # Heap stored as list
        return

    # returns the elements of the current data structure
    def show(self):
        """Returns a list containing the elements in the queue, heapified."""
        return self.h

    def is_empty(self):
        """Returns True if the priority queue is empty."""
        return len(self.h) == 0

    def enqueue(self, node):
        """Adds an element to the priority queue."""
        heappush(self.h, node)
        return

    def dequeue(self):
        """Removes an element from the priority queue."""
        return heappop(self.h)

    def size(self):
        """Returns the number of elements in the priority queue."""
        return len(self.h)

    def __contains__(self, item):
        """Overloads the 'in' Python operator."""
        return item in self.h
