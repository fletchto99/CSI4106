import functools


# Priority Queue Implementation of the data structure PriorityQueue.py
class PriorityQueue:
    # initializes the data structure
    def __init__(self, fct):
        self.items = []
        self.comparator = fct

    # returns the elements of the current data structure
    def show(self):
        return self.items

    # returns a boolean indicating whether the current data structure is empty or not
    def isEmpty(self):
        return not self.items

    # add the element item to the current data structure
    def enqueue(self, item):
        self.items.insert(0, item)

    # removes an element from the current data structure
    def dequeue(self):
        if self.isEmpty():
            raise Exception("Nothing in queue")
        # Re-organized the priority queue to ensure we pop the proper element
        self.items.sort(key=functools.cmp_to_key(self.comparator))
        return self.items.pop()

    # returns the size of the current data structure (the number of elements)
    def size(self):
        return len(self.items)

    # returns a boolean value that indicates if the element item is contained in the current data structure
    def __contains__(self, item):
        return item in self.items
