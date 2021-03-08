#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 12:42:47 2021

@author: yashwanthkumar
"""


## Double Linkedlist

# Node  Class
class Node():
    def __init__(self,val):
        # value to be stored
        self.val = val
        # pointer to the next node
        self.next = None
        # ponter to the previous node
        self.prev = None
        
class DoubleLinkedlist():
    def __init__(self):
        # sentinel head
        self.head = Node(None)
        # sentinel tail
        self.tail = Node(None)
        
        # for an empty list head and tail sentinels are pointed to each other
        self.head.next = self.tail
        self.tail.prev = self.head
        
        # size
        self.size = 0
        
        
    def addAtIndex(self,index, value):
        if index<0 or index>self.size:
            return False
        node = Node(value)
        if index < self.size - index:
            prev = self.head
            for _ in range(index):
                prev = prev.next
            curr = prev.next
        else:
            curr = self.tail
            for _ in range(self.size-index):
                curr = curr.prev
            prev = curr.prev
            
        node.next = curr
        node.prev = prev
        prev.next = node
        curr.prev = node
        
        self.size+=1
        return True
    
    def get(self,index):
        if index<0 or index > self.size-1:
            return
        if index < self.size-index:
            curr = self.head
            for _ in range(index+1):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size-index):
                curr = curr.prev
                
        return curr.val
    
    
    
    def deleteAtIndex(self,index):
        if index<0 or index > self.size-1:
            return False
        
        if index < self.size-index:
            prev = self.head
            for _ in range(index):
                prev = prev.next
            curr = prev.next.next
        else:
            curr = self.tail
            for _ in range(self.size-index-1):
                curr = curr.prev
            prev = curr.prev.prev
        
        prev.next = curr
        curr.prev = prev
        self.size -=1
        
        
        
    def print(self):
        curr = self.head
        for _ in range(self.size+1):
            print(" - {} ".format(curr.val),end = "->")
            curr = curr.next
        print(" - {} ".format(curr.val))
        print("\n")
        
        

        
        
lst = DoubleLinkedlist()
lst.addAtIndex(0,5)
lst.addAtIndex(1,55)
lst.addAtIndex(2,555)
lst.addAtIndex(3,5555)
lst.addAtIndex(4,55555)
print("Added 5 elements")
lst.print() 
print("printing some elements ") 
print(lst.get(2))     
print(lst.get(3)) 
print(lst.get(1)) 
print(lst.get(4)) 
print("Delete 1 element at 2 index")
lst.deleteAtIndex(2)
lst.print()  
print("Delete 1 element at 0 index")
lst.deleteAtIndex(0)
lst.print()      
        
        