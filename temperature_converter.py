# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 17:55:02 2020

@author: mchoubey
"""

"""
 F -> C = (F - 32) x 5/9
 F -> K = (F - 32)/1.8 + 273.15
 C -> F = (C x 9/5) + 32
 C -> K = C + 273.15
 K -> F = (K - 273.15) x 9/5 + 32
 K -> C = K - 273.15
"""
def f2c():
    f = float(input("Enter temperature in Fareinheit :- "))
    c = (f-32)*5/9
    print(f"Temperature in Celcius is {c}")
    
def f2k():
    f = float(input("Enter temperature in Fareinheit :- "))
    k = (f-32)/1.8 + 32
    print(f"Temperature in Kelvin is {k}")
def c2f():
    c = float(input("Enter temperature in Celcius :- "))
    print(f"Temperature in Fareinheit is {(c*9/5) + 32}")
def c2k():
    c = float(input("Enter temperature in Celcius :- "))
    print(f"Temperature in Kelvin is {c + 273.15}")
def k2f():
    k = float(input("Enter temperature in Kelvin :- "))
    print(f"Temperature in F is {(k-273.15) * 9/5 + 32}")
def k2c():
    k = float(input("Enter temperature in Kelvin :- "))
    print(f"Temperature in C is {k-273.15}")
    
if __name__ == '__main__':
   
    while(True):
        user = input("""Select one of the folowwing options:
            Type 'fc' to convert from Fahrenheit to Celsius.
            Type 'fk' to convert from Fahrenheit to Kelvin.
            Type 'cf' to convert from Celsius to
            Fahrenheit.
            Type 'ck' to convert from Celsius to Kelvin.
            Type 'kf' to convert from Kelvin to Fahrenheit.
            Type 'kc' to convert from Kelvin to Celsius.
            Enter input here:
            """)
        
    
        if user.casefold() == 'fc':
            f2c()
            break
        elif user.casefold() == 'fk':
            f2k()
            break
        elif user.casefold() == 'cf':
            c2f()
            break
        elif user.casefold() == 'ck':
            c2k()
            break
        elif user.casefold() == 'kf':
            k2f()
            break
        elif user.casefold() == 'kc':
            k2c()
            break
        else:
            print("Enter a correct selection >>>>>>")
    
    
    
    