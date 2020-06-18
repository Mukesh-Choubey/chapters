# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 18:37:24 2020

@author: mchoubey
"""
"""
EMI = Total/term
Total = Principal(1+ term * term)
Interest = P X r X t
"""
def loan():
    principal = float (input("Enter the total car loan amount :- "))
    term = float(input("Enter the loan term in months :- "))
    interest_rate = float(input("Enter your yearly rate of interest :- "))
    r = (interest_rate / 12) /100
    interest = principal * r * term
    Total = principal + interest
    EMI = Total/term
    print(f"EMI is {round(EMI)}, Total interest is {interest}, Total money is {Total}")
    
if __name__ == '__main__':
    loan()
    