### Author: Amal Zouaq
### azouaq@uottawa.ca
### Author: Hadi Abdi Ghavidel
### habdi.cnlp@gmail.com

# Used to create a comparator for sorting
import functools

from operator import attrgetter

#Queue - Implementation of the data structure Queue
class Queue:
    # initializes the current data structure
    def __init__(self):
        self.items = []

    # returns the elements of the current data structure
    def show(self):
        return self.items

    # returns a boolean indicating whether the current data structure is empty or not
    def isEmpty(self):
        return not self.items

    # add the element item to the current data structure
    def enqueue(self, item):
        self.items.insert(0,item)

    # removes an element from the current data structure
    def dequeue(self):
        if self.isEmpty():
            raise Exception("Nothing in queue")
        return self.items.pop()

    # returns the size of the current data structure (the number of elements)
    def size(self):
        return len(self.items)

    # returns a boolean value that indicates if the element item is contained in the current data structure
    def __contains__(self, item):
        return item in self.items


#Priority Queue Implementation of the data structure PriorityQueue.py
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

#Stack - Implementation of the data structure Stack
class Stack:
    # initializes the data structure
    def __init__(self):
        self.items = []

    # returns the elements of the current data structure
    def show(self):
        return self.items

    # returns a boolean indicating whether the current data structure is empty or not
    def isEmpty(self):
        return not self.items

    # add the element item to the current data structure
    def push(self, item):
        self.items.append(item)

    # removes an element from the current data structure
    def pop(self):
        if self.isEmpty():
            raise Exception("Nothing on stack")
        return self.items.pop()

    # returns the size of the current data structure (the number of elements)
    def size(self):
        return len(self.items)

    # returns a boolean value that indicates if the element item is contained in the current data structure
    def __contains__(self, item):
        return item in self.items

#Prints results for search alorithms
def printResults(alg, solution, start, stop, nbvisited):
    try:
        result, depth = solution.extractSolutionAndDepth()
        if result != []:
            print("The Solution is  ", (result))
            print("The Solution is at depth ", depth)
            print("The path cost is ", solution.getcost())
            print('Number of visited nodes:', nbvisited)
            time = stop - start
            print("The execution time is ", time, "seconds.")
            print("Done!")
    except AttributeError:
        print("No solution")
    except MemoryError:
        print("Memory Error!")
