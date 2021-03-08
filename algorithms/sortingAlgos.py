#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 23:18:42 2020

@author: yashwanthkumar
"""


s = [3,2,1,4,5,7,6,8]

"""
Algorithm: selection sort
Time Complexity: O(n^2)
Space Complexity: O(1)
"""
def selectionSort(arr):
    for i in range(len(arr)):
        min_idx =i
        for j in range(i+1,len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j      
        arr[min_idx],arr[i]=arr[i],arr[min_idx]
        
    return arr
                

print(selectionSort(s))



"""
Algorithm: bubble sort
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            pass
        pass
        
        
    pass







# merge sorted arrays
lst1 = [1,4,6,8,11]
lst2 = [2,3,5,9,14,19,21]

lst1 =None
lst2 = None


def merge_sorted_arrays(lst1,lst2):
    if lst1 is None and lst2 is None:
        return []
    if lst1 is None:
        return lst2
    if lst2 is None:
        return lst1
    l1 =len(lst1)
    l2 = len(lst2)
    result =[]
    p1,p2=0,0
    while p1<l1 and p2<l2:
        if lst1[p1]<lst2[p2]:
            result.append(lst1[p1])
            p1 +=1
        else:
            result.append(lst2[p2])
            p2 +=1
            
            
    while p1<l1:
        result.append(lst1[p1])
        p1+=1
    while p2<l2:
        result.append(lst2[p2])
        p2+=1
        
    return result

print(merge_sorted_arrays(lst1,lst2))

lst2 = [1,4,6,8,11]
lst1 = [2,3,5,9,14,19,21,0,0,0,0,0]






    
    
"""
ALGORITHMS
"""  
# Selection Sort
arr =[2,5,1,4,3,6,9,8,10]

def selection_sort(arr):
    array_size=len(arr)
    if array_size==0:
        return None
    if array_size==1:
        return arr
    for i in range(array_size):
        min_index = i
        for j in range(i+1,array_size):
            if arr[j]<arr[min_index]:
                min_index=j
        if min_index!=i:
            arr[min_index],arr[i]=arr[i],arr[min_index]
            
    return arr

print(selection_sort(arr))

    
def bubble_sort(arr):
    array_size =len(arr)
    if array_size==0:
        return None
    if array_size==1:
        return arr
    for i in range(array_size):
        for j in range(0,array_size-1-i):
            if arr[j+1]<arr[j]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
                
    return arr


print(bubble_sort(arr))



def insertion_sort(arr):
    array_size=len(arr)
    for i in range(0,len(arr)):
        key = arr[i]
        j=i-1
        while j>0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
        
    return arr

print(insertion_sort(arr))




# merge sort
# time complexity - nlog(n)
arr = [5,4,3,6,2,7,1,8,10]

def merge_sort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        right = arr[:mid]
        left = arr[mid:]
        
        merge_sort(right)
        merge_sort(left)
        
        # combine the list
        i=0
        j=0
        k=0
        while i<len(right) and j < len(left):
            if right[i] < left[j]:
                arr[k]=right[i]
                i+=1
            else:
                arr[k]=left[j]
                j+=1
            k+=1
            
        # fill the rest
        # fill right if present
        while i<len(right):
            arr[k]=right[i]
            i+=1
            k+=1
        # fill left if present
        while j<len(left):
            arr[k]=left[j]
            j+=1
            k+=1
        
    return arr
            
print(merge_sort(arr))    

            
# quick sort
arr = [5,4,3,6,2,7,1,8,10]



def partition(arr,left,right):
    pivot_idx = (left+right)//2
    while left<right:
        while arr[left]<arr[pivot_idx]:
            left+=1
        while arr[right]>arr[pivot_idx]:
            right-=1
        if left>=right:
            return left
        else:
            arr[left],arr[right]=arr[right],arr[left]


def quick_sort(arr,left,right):
    if left<right:
        pivot = partition(arr,left,right)
        quick_sort(arr,left,pivot)
        quick_sort(arr,pivot+1,right)
    
      
def quick_sort_helper(arr):
    quick_sort(arr,0,len(arr)-1)
    return arr
    
print(quick_sort_helper(arr))





# quick sort
arr = [5,4,3,6,2,7,1,8,10]
left_idx = 0
right_idx = len(arr)-1
pivot = (left_idx + right_idx)//2
print(pivot)


while left_idx<right_idx:
    while arr[left_idx]<pivot:
        left_idx+=1
    while arr[right_idx]>pivot:
        right_idx-=1
    if left_idx>right_idx:
         print(left_idx)
    else:
        arr[right_idx],arr[left_idx]=arr[left_idx],arr[right_idx]

print(arr)

arr = [5,4,99,3,6,2,7,1,8,10,45]
arr= [5,6,3,4,2,1,0,9,22,45,23]



arr=[9,7,8,6,4,5,3,3,66,2,44,1,22,77,11,99,33,24,13,58]

arr = [5,4,3,6,2,7,1,8,10, -3, 4, -3, -7,2,0,1,9, 2, 5, 0, -3, -3, 2]




arr=[9,7,8,6,4,5,3,3,66,2,44,1,22,77,11,99,33,24,13,58]



#arr = [5,4,3,6,2,7,1,8,10]
def choose_pivot_index(arr,left_idx,right_idx):
    # midpoint
    pivot = (left_idx+right_idx)//2
    return pivot

def partition_list(arr,left_idx,right_idx):
    pivot_idx = choose_pivot_index(arr,left_idx,right_idx)
    pivot = arr[pivot_idx]
    #left_idx -= 1
    #right_idx += 1
    while left_idx<=right_idx: 
        while arr[left_idx] < pivot:
            left_idx+=1
        while arr[right_idx] > pivot:
            right_idx-=1
        if left_idx<right_idx:
            # return the index by which the list is divided into 2. 
            # Since the elements are rearranged based on pivot, this index 
            # will contain the pivot element
            arr[left_idx],arr[right_idx]=arr[right_idx],arr[left_idx]
        else:
            return right_idx
        left_idx+=1
        right_idx-=1
    return right_idx

    
    
def quick_sort_recursive(arr,left_idx,right_idx):
    if left_idx < right_idx:
        # at the end of partition the index returned will be having the pivot element 
        # because of the partition logic
        pivot_idx = partition_list(arr,left_idx,right_idx)
        quick_sort_recursive(arr,left_idx,pivot_idx)
        quick_sort_recursive(arr,pivot_idx+1,right_idx)
    

def quick_sort(arr):
    quick_sort_recursive(arr,0,len(arr)-1)
    return arr


print(quick_sort(arr))



"""
Search

"""
# linear search
arr = [5,4,3,6,2,7,1,8,10]

def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] ==target:
            return i
    return -1

print(linear_search(arr,8))



# binary search for sorted array

arr =[1, 2, 3, 4, 5, 6, 7, 8, 10]
def binary_search(arr,target):
    array_size = len(arr)
    mid = array_size//2
    while mid>0:
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            mid = mid-((mid-array_size)//2)
        else:
            mid = mid + ((mid-array_size)//2)
    return -1

print(binary_search(arr,4))