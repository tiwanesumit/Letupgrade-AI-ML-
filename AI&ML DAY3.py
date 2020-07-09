# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 10:49:35 2020

@author: DELL
"""

#Write a program to subtract two complex numbers in Python.

a = 5+2j
b = 3+1j

z= a -b
print(z)

#Write a program to find the fourth root of a number.

a = 5

x = a**4

print(x)


#Write a program to swap two numbers in Python with the help of a temporary variable.

R = 55

T = 77

tempvar = R

R = T

T = tempvar

print('The value of R after swapping',R)
print('The value of T after swapping',T)


#Write a program to swap two numbers in Python without using a temporary variable.


x = 100
y = 50
   
x = x + y   
y = x - y  
  
x = x - y   

print("After Swapping x =", x, " y =", y);


#Write a program to convert fahrenheit to kelvin and celsius both.

def Fahrenheit_to_Kelvin(F): 
    return 273.5 + ((F - 32.0) * (5.0/9.0)) 

F = 110
print("Temperature in Kelvin ( K ) = {:.3f}" 
            .format(Fahrenheit_to_Kelvin( F ))) 

#Write a program to demonstrate all the available data types in Python
'''
*list
*tuple
*Number
*string
*set
*dictionary
'''












