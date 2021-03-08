#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 15:18:58 2021

@author: yashwanthkumar
"""

lst = [1,21,3,14,5,60,7,6]
k = 81
def target_sum(lst,target):
    visited_num = {}
    for num in lst:
        if target-num in lst:
            return [num,target-num]
        else:
            visited_num[num]=1
            
    return [-1,-1]


print(target_sum(lst,k))
            
            
            
          
list(range(5,0,-1))
                  
            
            
            
arr = [1,2,3,4]



def multiply_except_self(arr):
    output = []
    n = len(arr)
    last_idx =n-1
    print("length : {}".format(n))
    output.append(1)
    for idx in range(1,n):
        output.append(arr[idx-1]*output[idx-1])
    print(output)
    right=1
    for i in range(n):
        print(i)
        print(last_idx-i)
        output[last_idx-i] = output[last_idx-i]*right
        right *= arr[last_idx-i]
    return output
    
print(multiply_except_self(arr))




arr = [9,2,4,3,2,6,6,9]
def find_first_unique_element(arr):
    for i in range(len(arr)):
        cnt=0
        for j in range(len(arr)):
            if i!=j and arr[i]==arr[j]:
                break
            cnt +=1
        if cnt== len(arr):
            return arr[i]
        
    return None


print(find_first_unique_element(arr))
                





import sys
arr =[9,2,3,6]
def find_second_max(arr):
    max1,max2= -sys.maxsize,-sys.maxsize
    for element in arr:
        if element > max1:
            max2=max1
            max1=element
        elif element > max2:
            max2=element
            
    return max2

print(find_second_max(arr))
        
    
    
lst = [10,20,30,40,50,60,70,80,90,100]
n = 4


def rotate_right_brute_force(arr,k):
    array_size = len(arr)
    result = []
    for i in range(array_size-k,array_size):
        result.append(arr[i])
        
    for j in range(array_size-k):
        result.append(arr[j])
    return result

print(rotate_right_brute_force(lst,n))



def rotate_right(arr,k):
    if len(arr) ==0 or k>=len(arr):
        return None
    s=0
    e =len(arr)-1
    # reverse the entire array
    while s<e:
        arr[s],arr[e]=arr[e],arr[s]
        s+=1
        e-=1
    # reverse the first k elements
    s=0
    e= k-1
    while s<e:
        arr[s],arr[e]=arr[e],arr[s]
        s+=1
        e-=1
    # reverse the rest of the elemnts
    s=k
    e=len(arr)-1
    while s<e:
        arr[s],arr[e]=arr[e],arr[s]
        s+=1
        e-=1
    return arr


print(rotate_right(lst,n))
    



# move neg towards left and positive towards right
arr = [10,-1,20,4,5,-9,-6]
def move_pos_neg_brute_force(arr):
    res= []
    for element in arr:
        if element<0:
            res.append(element)
            
    for element in arr:
        if element >=0:
            res.append(element)
            
    return res

print(move_pos_neg_brute_force(arr))
    

def move_pos_neg_sol1(arr):
    s=0
    e=len(arr)-1
    while s<e:
        if arr[s]<0:
            s+=1
        if arr[e]>=0:
            e-=1
        if arr[s]>=0 and arr[e]<0:
            arr[s],arr[e]=arr[e],arr[s]
            s+=1
            s-=1
    return arr

print(move_pos_neg_sol1(arr))



def move_pos_neg_sol2(arr):
    s=0
    e=len(arr)-1
    while True:
        while s<0:
            s+=1
        while e>=0:
            e-=1
        if s>=e:
           break
        arr[s],arr[e]=arr[e],arr[s]
        s+=1
        e-=1
    return arr

print(move_pos_neg_sol2(arr))


arr = [-34,10,-1,20,4,5,-9,-6]
def move_pos_neg_sol3(arr):
    left_pos_idx=0
    for i in range(len(arr)):
        if arr[i]<0:
            if i is not left_pos_idx:
                arr[i],arr[left_pos_idx]=arr[left_pos_idx],arr[i]
            left_pos_idx+=1
    return arr


print(move_pos_neg_sol3(arr))            





# rearrange to max min form
arr = [1,2,3,4,5]

def rearrange(arr):
    res = []
    max_index = len(arr)-1
    min_index = 0
    for i in range(len(arr)):
        if i%2==0:
            res.append(arr[max_index])
            max_index -= 1
        else:
            res.append(arr[min_index])
            min_index += 1
    return res

print(rearrange(arr))





# maximum subarray sum
arr = [-2,10,7,-5,15,6]

def max_subarray_sum_brute_force(arr):
    array_sum =0
    for i,element in enumerate(arr):
        curr_sum=element
        for j in range(i+1,len(arr)):
            curr_sum+=arr[j]
            if curr_sum >array_sum:
                array_sum = curr_sum
    return array_sum
            
            
print(max_subarray_sum_brute_force(arr))   



import sys

def max_subarray_kadane(arr):
    global_maxima = -sys.maxsize
    local_maxima = 0
    for i in range(len(arr)):
        local_maxima = max(arr[i],arr[i]+local_maxima)
        if local_maxima > global_maxima:
            global_maxima = local_maxima
    return global_maxima

print(max_subarray_kadane(arr))




