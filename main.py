from art import logo, vs
from game_data import data
import random


# format the account data into printable format 
def format_data(account):
    """format the account data into printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name},a {account_descr}, from {account_country}"
    
# use if statement to compare and check if user is correct
def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and return if user got it right"""
    if a_followers > b_followers:
        # if guess == "a":
        #     return True
        # else:
        #     return False
        return guess == "a"
    else:
        return guess == "b"


#display art
print(logo)

# generate a random account from the game data
account_a = random.choice(data)
print(account_a)
account_b = random.choice(data)
print(account_b)
if account_a == account_b:
    account_b = random.choice(data)

print(f"Compare A : {format_data(account_a)}")
print(vs)
print(f"Against B : {format_data(account_b)}")

#ask user for a guess.
guess = input("Who has more followers ? Type 'A' or 'B': ").lower()

#check if user is correct
## get the follower count of each account
a_follower_acount = account_a["follower_count"]
b_follower_acount = account_b["follower_count"]


#give user feedback on their guess.

#keep score +1 if user guess is correct. End game if wrong and display score

#make game repeatable if user is right. recursive game()

#make account position B become the next account at position A

#clear the terminal screen between rounds.
