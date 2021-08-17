# Course: CS261 - Data Structures
# Student Name: Jonathon Stoddart
# Assignment: 5
# Description: Part 2 - Min Heap Implementation


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        Adds a new object to the MinHeap maintaining heap property (every node's value is less than or equal to those
        of its children).
        """
        self.heap.append(node)
        self.percolate_up(self.heap.length()-1)

    def percolate_up(self, idx):
        """
        Percolates an object in the heap up until its priority value is less than both of its children.
        """
        parent_idx = (idx - 1) // 2

        while idx !=0 and self.heap.get_at_index(idx) < self.heap.get_at_index(parent_idx):
            # swap with parent
            temp = self.heap.get_at_index(parent_idx)
            self.heap.set_at_index(parent_idx, self.heap.get_at_index(idx))
            self.heap.set_at_index(idx, temp)
            # update pointers
            idx = parent_idx
            parent_idx = (idx - 1) // 2

    def get_min(self) -> object:
        """
        Returns an object with a minimum key without removing it from the heap. If the heap is empty, raises 
        MinHeapException.
        """
        if self.heap.length() == 0:
            raise MinHeapException

        return self.heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        Returns an object with a minimum key and removes it from the heap. If the heap is empty, the method raises
        MinHeapException
        """
        if self.heap.length() == 0:
            raise MinHeapException

        original_min = self.heap.get_at_index(0)

        # replace root with last element in heap and percolate down
        self.heap.set_at_index(0, self.heap.get_at_index(self.heap.length()-1))
        self.heap.pop()
        
        if self.heap.length() > 0:
            self.percolate_down(0)

        return original_min

    def percolate_down(self, idx) -> None:
        """
        Percolates an object in the heap down until its priority value is not greater than either of its children,
        or it has reached the bottom of the heap.
        """
        min_idx = self.get_min_idx(idx)

        while min_idx is not None and self.heap.get_at_index(idx) > self.heap.get_at_index(min_idx):
            temp = self.heap.get_at_index(min_idx)
            self.heap.set_at_index(min_idx, self.heap.get_at_index(idx))
            self.heap.set_at_index(idx, temp)
            idx = min_idx
            min_idx = self.get_min_idx(idx)

    def get_min_idx(self, idx) -> int:
        """
        Returns the index of the smaller child of the object at heap index "idx".
        """
        lchild_idx = 2 * idx + 1
        rchild_idx = 2 * idx + 2
        
        if lchild_idx >= self.heap.length():  # both elements fall beyond bounds of array, stop
            return None

        if rchild_idx >= self.heap.length():  # one child only
            return lchild_idx
        
        if self.heap.get_at_index(lchild_idx) > self.heap.get_at_index(rchild_idx):  # two children
            return rchild_idx
        else:
            return lchild_idx

    def build_heap(self, da: DynamicArray) -> None:
        """
        Receives a dynamic array with objects in any order and builds a proper MinHeap from them.
        Current content of the MinHeap is lost.
        """
        # copy da to heap
        self.heap = DynamicArray()
        for i in range(da.length()):
            self.heap.append(da.get_at_index(i))
        
        # starting with leaves (reverse) find nodes that violate heap property and percolate down
        for i in range(self.heap.length()-1, -1, -1):
            if self.get_min_idx(i) is not None:
                self.percolate_down(i)


# BASIC TESTING
if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)


    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())


    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())


    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([53, 29, 34, 32, 44, 11, 21, 18, 66, 25, 15, 20])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)
