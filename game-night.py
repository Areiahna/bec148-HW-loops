# Task 1: Random Choice Game 

# Create a game where a player has a list of items. They have to guess which item in the list was selected. Use random.choice() to select the item and take the user's guess via input. Provide feedback on whether they guessed correctly or not keep them playing until they guess correctly.
import random

nums = [1,2,3,4,5,6,7,8,9,10]

while True:
    current_num = random.choice(nums)
    # print(current_num)
    guess = input("Guess a number 1 - 10:  ")
    
    if (int(guess) == current_num):
        print("OH MY! Can you read minds??")
        break
    else:
        print("Sorry friend... TRY AGAIN")