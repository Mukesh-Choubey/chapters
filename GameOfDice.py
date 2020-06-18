# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 19:05:24 2020

@author: mchoubey
"""
guess = 0
from random import randint
print("Welcome to the game of Dice")
bank = 1000
while True:
    print("How much money do you want to bet on :-")
    bet = float(input("How much money you want to bet:-"
                    f"your bank has {bank}:-"))
    if bet > 0 and bet <=bank:
        dice = randint(1,6)
        guess = int(input("Bet on a number between 1 and 6 :- "))
        if guess == dice:
            bank += 2*bet
            print(f"ITS YOUR LUCKY DAY Contgrats dice landed on your lucky number {dice}")
            print(f"You won {2*bet}, your new bank balance is ${bank}")
        else:
            bank -= bet
            print(f"Sorry, better luck next time, your lost ${bet}, number was {dice}, your balance is ${bank}")
        if bank <= 0:
            print(f"Game over, you have no money left")
            break
        play_again = input("Do you want to play again, say 'y' or 'n' :-").lower()
        if play_again == 'y':
            continue
        else:
            print("Game over")
            if bank > 1000:
                print(f"You are walking home richer, you earned ${bank-1000}")
                break
            else:
                print(f"Better luck next time, you lost ${1000-bank}")
            break
    else:
        print(f"Enter what you can afford,you only have ${bank} money left")
        
            
            
        
        
