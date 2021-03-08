#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 18:31:02 2021

@author: yashwanthkumar
"""

"""
Heap is used in implementing Priority Queues:

- Heap must be a complete binary trees

Properties of complete Binary Trees:
    1. All leaves are at depth d or d-1
    2. There can just one node hapen to have one child - means that here can be only one single child instance
    3. Incase of Singular child, The child node will be on left side of the parent node
    4. Incase of Singular child, The child node will be on the right most at depth d
    
Heap Property:
    Max Heap Property:
        All Parent Node elements >= It's child Node elements
        
    Min Heap Property:
        All Parent Node elements <= It's child Node elements
        

Heap  - Data structure used when you want to get the min or max in 0(1) time.
Adding takes O(log(N)) - 

There are 2 types of heap -> MinHeap / MaxHeap

Now we will implement both.

Heaps can be implemented using arrays/list


"""



# example of heap in array
import math
heap = [100,60,80,30,50,70,75,20,10,40]
num_of_parents = math.floor((len(heap)-1)/2)+1
print("Number of parents is Floor(Length-1)/2 => {}".format(math.floor((len(heap)-1)/2)))

for k in range(num_of_parents):
    print("Parent at Depth {} : {}".format(k,heap[k]))
    if 2*k+2<len(heap):
        print("Child to  Parent {}  is : {} - {}".format(heap[k],heap[2*k+1],heap[2*k+2]))
    else:
        print("Child to  Parent {}  is : {}".format(heap[k],heap[2*k+1]))

"""
Some facts:
    Not all the elements in a heap are sorted, just the root node is max/min.
    Heaps/Binary heaps are same -> since they are from binary tress.
    Heap Datastructure is different from Heap Memory.

"""

# Building Max Heap



class MaxHeap():
    def __init__(self):
        self.heap=[]
    
    def insert(self,val):
        self.heap.append(val)
        self._percolateUp(len(self.heap)-1)
    
    def getMax(self):
        if self.heap:
            return self.heap[0]
        else:
            return None
    
    def removeMax(self):
        if len(heap)>1:
            max_element = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self._maxHeapify(0)
            return max_element
        elif len(heap)==1:
            max_element = self.heap[0]
            return max_element
        else:
            return None
            
        
    
    def _percolateUp(self,index):
        parent = (index-1)//2
        if index<=0:
            return
        if self.heap[parent]<self.heap[index]:
            self.heap[parent],self.heap[index]=self.heap[index],self.heap[parent]
            self._percolateUp(parent)
    
    
    def _maxHeapify(self,index):
        left = 2*index +1
        right = 2*index +2
        largest_index = index
        if len(self.heap)>left and self.heap[largest_index] < self.heap[left]:
            largest_index = left
        if len(self.heap)>right and self.heap[largest_index] < self.heap[right]:
            largest_index = right
        if largest_index!= index:
            self.heap[largest_index],self.heap[index]=self.heap[index],self.heap[largest_index]
            self._maxHeapify(largest_index)
            
            
    def buildHeap(self,array):
        self.heap = array
        for i in range(len(array)-1,-1,-1):
            self._maxHeapify(i)



heap = MaxHeap()
heap.insert(12)
heap.insert(10)
heap.insert(-10)
heap.insert(100)

print(heap.getMax())    
    















