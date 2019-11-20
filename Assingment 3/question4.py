# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 23:03:41 2019

@author: HomeUser
"""

dic = {
    'num1' : 10,
    'num2' : 17,
    'string':'Name',
    'char':'a',
    'num3' : 12,
    'num4':31,
}

sum = 0

for i in dic.values():
    if type(i) == int:
        sum +=i

print("Sum of all numeric items a dictionary is" , sum)