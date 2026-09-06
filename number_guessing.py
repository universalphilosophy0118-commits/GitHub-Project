import random 

number = random.randint(1, 10)
attempts = 0

while True:
    attempts += 1
    guess = int(input("Guess the number:"))
    if guess < 1 or guess > 10:
       print("Please enter a number between 1 and 10.")
       continue
    if guess == number:
     print("Correct! You got it in", attempts, "attempts.")       
     break
    else:
        if guess > number:
            print("Too high!")
        else:
            print("Too low!")
    
    