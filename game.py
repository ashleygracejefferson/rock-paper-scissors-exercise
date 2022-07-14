# this is the "game.py" file...

print("Welcome 'Player One' to my Rock, Paper, Scissors, game!")

x=input("Please select rock. paper, or scissors:").lower()
print(x)

if x!="rock" and x!="paper" and x!="scissors":
    print("Please try again") 
    exit()

