# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 22:14:23 2019

@author: HomeUser
"""
val1=input('enter first number ')
val2=input('enter second number ')
operator = input('enter operator ')
val1 = int(val1)
val2 = int(val2)

if operator == '+':
    val = val1 + val2
    print(val,'answer')
    
elif operator == '-':
    val = val1 - val2
    print(val,'answer')
    
elif operator == '*':
    val = val1 * val2
    print(val,'answer')
    
elif operator == '/':
    val = val1 / val2
    print(val,'answer')
    
else:
    print('enter correct operator')
    