# this is the "game.py" file...

import random
print("Welcome 'Player One' to my Rock, Paper, Scissors, game!")

x=input("Please select rock. paper, or scissors:").lower()
print("You chose:"+ x)

if x!="rock" and x!="paper" and x!="scissors":
    print("Please try again") 
    exit()

choices =["rock","paper","scissors"]

y=random.choice(choices)

print("Computer chose:"+ y)

if x=="rock":
    if y=="rock":
        print("You have tied the game!")

    if y=="paper":
        print("You lose")
    
    if y=="scissors":
        print("You win!")

if x=="paper":
    if y=="rock":
        print("You win!")

    if y=="paper":
        print("You have tied the game!")
    
    if y=="scissors":
        print("You lose")

if x=="scissors":
    if y=="rock":
        print("You lose!")

    if y=="paper":
        print("You win!")
    
    if y=="scissors":
        print("You have tied the game!")

print("Thanks for playing, please play again!")
