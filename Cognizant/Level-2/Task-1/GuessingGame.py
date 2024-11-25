import random

num = random.randint(1, 100)

guess = int(input("Guess a number between 1 to 100:"))

while(guess in range(1,100)):
    
    if num == guess:
        print("Your guess is correct ")
        break
    
    elif num < guess:
        print("Hint: your guess is too high")
        guess = int(input("Guess again:"))
        
    elif num > guess:
        print("Hint: your guess is too low")
        guess = int(input("Guess again:"))