# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 21:32:55 2019

@author: HomeUser
"""

def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list([4, 6, -8, 98]))