#display art
from art import logo
from game_data import data
import random

# generate a random account from the game data

print(logo)
account_a = random.choice(data)
print(account_a)
account_b = random.choice(data)
print(account_b)

# format the account data into printable format 

#ask user for a guess.

#check if user is correct
## get the follower count of each account
## use if statement to compare and check if user is correct

#give user feedback on their guess.

#keep score +1 if user guess is correct. End game if wrong and display score

#make game repeatable if user is right. recursive game()

#make account position B become the next account at position A

#clear the terminal screen between rounds.
