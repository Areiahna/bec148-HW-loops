# Task 1: Loop Condition Exploration Write a while loop with a condition that will never be true (an infinite loop). Ask the user a question until their answer triggers a break statement (hint: use an if statement to evaluate their answer).


while True:
    fav_anime = input("What's THE BEST anime? ")

    if (fav_anime == "one peice"):
        print("I will be King of Pirates!")
        break
    else:
        print("SURVEY SAYS: [X][X][X]")
    
print("="*50)
#-----------------------------

# Task 2: Conditional Exit 

# Create a while loop that will terminate after 5 iterations, and each iteration you print which iteration it is on. (use a control variable)

tokens = 5

while (tokens >= 1): 
    tokens -= 1
    print("GAME OVER!!", tokens, "TOKENS LEFT")
    