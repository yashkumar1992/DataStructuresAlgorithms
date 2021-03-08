#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 12:42:42 2021

@author: yashwanthkumar
"""



# Singly Linkedlist
# Node  Class
class Node():
    def __init__(self,val):
        # value to be stored
        self.val = val
        # pointer to the next node
        self.next = None
        



class SingleLinkedlist():
    def __init__(self):
        # initialize head as None
        self.head = Node(None)
        # No element is present at the time of initialization
        self.size = 0
        
    def get(self,index):
        if index <0 or index > self.size-1:
            return
        curr = self.head
        for _ in range(index+1):
            curr = curr.next
        return curr.val
            
        
    def addAtIndex(self,index, val):
        node = Node(val)
        if index < 0 or index > self.size:
            return False
        curr = self.head
        for _ in range(index):
            curr = curr.next
        node.next = curr.next
        curr.next = node
        self.size +=1
        return True
    
    def deleteAtIndex(self,index):
        if index < 0 or index > self.size-1:
            return False
        
        prev = self.head
        curr = prev.next
        for _ in range(index):
            prev = curr
            curr = curr.next
        prev.next = curr.next
        self.size -=1
        return True
            
    
    def print(self):
        curr = self.head
        for _ in range(self.size+1):
            print(" - {} ".format(curr.val),end = "->")
            curr = curr.next
        print("\n")
        
   
        

# Singly Linked List
lst = SingleLinkedlist()
lst.addAtIndex(0,1) 
lst.print()
lst.addAtIndex(1,3) 
lst.print()   
lst.addAtIndex(1,2) 
lst.print() 
print("Get element at {}".format(1))
print(lst.get(1))
lst.deleteAtIndex(1) 
lst.print() 
print("Get element at {}".format(1))
print(lst.get(1))
lst.print() 



# Singly Linked List
lst = SingleLinkedlist()
lst.addAtIndex(0,5)
lst.addAtIndex(1,55)
print("Added 2 elements")
lst.print()
print("Del 1 element  at index 0")
lst.deleteAtIndex(1)
lst.print()
print("Del 1 element  at index 1")
lst.deleteAtIndex(0)
lst.print()
print("Added 2 elements")
lst.addAtIndex(0,5)
lst.addAtIndex(1,55)
lst.print()
        

