import random
min = int(input("Enter minimum value:"))
max = int(input("Enter maximum value:"))

num = random.randint(min,max)

guess = int(input("Guess a number between " + str(min) +" to "+ str(max) + ":"))

while(guess in range(min,max)):
    
    if num == guess:
        print("Your guess is correct ")
        break
    
    elif num < guess:
        print("Hint: your guess is too high")
        guess = int(input("Guess again:"))
        
    elif num > guess:
        print("Hint: your guess is too low")
        guess = int(input("Guess again:"))
