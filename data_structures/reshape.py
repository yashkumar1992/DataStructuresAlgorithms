#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 16:45:11 2021

@author: yashwanthkumar
"""


arr = [1,2,3,4,5,6,7,8]

#arr = [1,2,3,4]

out = [[1,2],[3,4]]


def reshape(arr,shape):
    m,n=shape
    if len(arr)!= m*n or len(arr)==0:
        return None
    result=[]
    
    for i in range(m):
        temp_arr=[]
        for j in range(n):
            temp_arr.append(arr[(i*n)+j])
        
        result.append(temp_arr)
    
    return result

print(reshape(arr,(4,2)))
    