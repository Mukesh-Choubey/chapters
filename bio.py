# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 17:18:25 2020

@author: mchoubey
"""
def questions():
    first_name = (input("Enter your first name:- ")).capitalize()
    last_name = (input("Enter your last name:- ")).capitalize()
    nationality = input("Enter you nationality:- ")
    birth_place = input("Enter your city of birth:- ")
    age = int(input("Enter your age:- "))
    height_raw = input("Enter your height in feet and inches seperated by comma:- ")
    height_raw= height_raw.split(',')
    height = height_raw[0], height_raw[1]
    weight = float(input("Enter your weight in lbs :- "))
    print()
    print(f"Hi ! My name is {first_name} {last_name}")
    print(f"I am an {nationality}")
    print(f"I was born in {birth_place}")
    print(f"My age is {age} years")
    print(f"I am {height[0]} feet {height[1]} inches tall")
    print(f"I am {weight} lbs heavy")
    
    
    
if __name__ == '__main__':
    questions()    
