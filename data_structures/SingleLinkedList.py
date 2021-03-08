#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 18:04:48 2021

@author: yashwanthkumar
"""

"""
Single Linkedlist

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

"""



class Node():
    def __init__(self,val):
        self.val = val
        self.next = None
    
class SingleLinkedlist():
    def __init__(self):
        self.head= Node(None)
        self.size = 0
        
    def insert_at_index(self,val,index):
        node = Node(val)
        if index > self.size:
            return False
        i=0
        currNode = self.head
        while i<index:
            currNode =  currNode.next
            i+=1
        node.next = currNode.next
        currNode.next = node
        self.size +=1
        return True
    
    def insert_at_head(self,val):
        self.insert_at_index(val,0)
        
    def insert_at_tail(self,val):
        self.insert_at_index(val,self.size-1)
        
    def get_by_index(self,index):
        currNode = self.head
        i=0
        while i<index and index < self.size-1:
            currNode = currNode.next
            i +=1
        return currNode
    
    def delete_by_index(self,index):
        if index > self.size:
            return False
        prev = self.head
        curr = self.head.next
        i = 0
        while i<index:
            prev = curr
            curr = curr.next
            i +=1
        prev.next = curr.next
        return True
        
            
    
    def print(self):
        node = self.head.next
        print("Null -> ",end='')
        while node is not None:
            print("{} -> ".format(node.val),end='')
            node = node.next
        print("Null")
    
    
lst = SingleLinkedlist()
lst.insert_at_index(3,0)
lst.insert_at_index(33,0)
lst.insert_at_index(333,0)
lst.insert_at_index(3333,0)
lst.insert_at_index(33333,0)
lst.print()
lst.insert_at_index(333333,5)
lst.insert_at_index(3333333,5)
lst.print()
lst.delete_by_index(0)
lst.print()
lst.delete_by_index(0)
lst.print()
lst.delete_by_index(2)
lst.print()
        
          





                      
            