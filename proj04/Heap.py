import math
import statistics
import pandas as pd
class Heap:
    """
    A heap-based priority queue
    Items in the queue are ordered according to a comparison function
    """

    def __init__(self,comp):
        """
        Constructor
        :param comp: A comparison function determining the priority of the included elements
        """
        self.heap=[]
        self.comp = comp
        self.size = 0
        # Added Members

    def __len__(self):
        return len(self.heap)
    
    def peek(self):
        if(self.is_empty()):
            raise IndexError
        return self.heap[0]

  

    def insert(self, item):
        """place value at an available leaf, then bubble up from there"""
        self.heap.append(item)
        self.size +=1
        print("before inv_heapify",self.heap)
        self._inv_heapify(self.size-1)
        print("inv_heapify applied",self.heap)

        pass

    def extract(self):
        print("before pop",self.heap)
        if(self.is_empty()):
            raise IndexError
        result = self.heap[0]
        self.heap[0] =self.heap[-1]
        self.heap.pop()
        self.size-=1
        print("after pop",self.heap)
        self.heapify(0)
        print("heapifying the heap",self.heap)
        
        return result
      
    def extend(self, seq):
        self.heap.extend(seq)
        for item in range(len(self)//2,-1,-1):
            self.heapify(item)

    def clear(self):
        self.heap.clear()
        

    def __iter__(self):
          for item in self.heap:
              yield item
    # Supplied methods

    def __bool__(self):
        """
        Checks if this heap contains items
        :return: True if the heap is non-empty
        """
        return not self.is_empty()

    def is_empty(self):
        """
        Checks if this heap is empty
        :return: True if the heap is empty
        """
        return len(self) == 0

    def __repr__(self):
        """
        A string representation of this heap
        :return:
        """
        return 'Heap([{0}])'.format(','.join(str(item) for item in self))

    # Added methods
    def heapify(self, root_index):
        """
        Do heapifying starting from root till it reaches leaf with no children
        """
        heap, compare = self.heap, self.comp
        length = len(heap)
#        print(heap)
        if length == 1:
            return
        parent = root_index
        while 2 * parent+1 < length:
            child = 2 * parent+1#left child
            if (child  and child + 1< length) and (compare(heap[child + 1], heap[child])):# If both the left and right child are within our bounds
                child += 1#And they do not violate our heap priority structure we will move on to the next left child
            if compare(heap[parent], heap[child]):
                return
            heap[parent], heap[child] = heap[child], heap[parent]
            parent = child
            print("swap made",heap)
        
    def _inv_heapify(self, child_index):
        """
        Do heapifying starting from bottom till it reaches the root.
        """
        heap, comp = self.heap, self.comp
        child = child_index
        while child > 0:#While we arent at the 0th index 
            parent = math.floor((child-1) // 2)
            if (comp(heap[parent], heap[child])):#Check to see if parent's priority is gretaer than the child
                return 
            else:
                heap[parent], heap[child] = heap[child], heap[parent]#If we find that the child has greater value than the parent we need to flip them
                child = parent
                print("swap made",heap)

def find_median(seq):
    """
    Finds the median (middle) item of the given sequence.
    Ties are broken arbitrarily.
    :param seq: an iterable sequence
    :return: the median element
    """
    if not seq:
        raise IndexError
    else:    
        min_heap = Heap(lambda a, b: a <= b)
        max_heap = Heap(lambda a, b: a >= b)
    
        item =((len(seq))-1)
        min_heap.extend(seq[:item])
        max_heap.extend(seq[item:])
    
        minpeek =  min_heap.peek()
        maxpeek  = max_heap.peek()
        while minpeek < maxpeek:
            min_heap.extract()
            max_heap.extract()
            min_heap.insert(maxpeek)
            max_heap.insert(minpeek)
            minpeek = min_heap.peek()
            maxpeek = max_heap.peek()
        return max_heap.peek()
           #Counting Sort
#    frequency_arry =[]
#    median_index =(len(seq)/2)
#    result_sum = 0
#    frequency_arry = seq
#    frequency_arry= np.bincount(frequency_arry)#Count number of instnaces of an element in a the seq arry
##    print(frequency_arry)
#    for items in frequency_arry:
#        result_sum+= items #Sum up the  values until we reach the median index 
#        if result_sum >= median_index:
#            return math.floor(result_sum)# Once result sum becomes >= to the median index we have found our median
       
    
