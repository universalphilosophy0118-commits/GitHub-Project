import random
choices = ["rock", "paper", "scissors"]
games = 0
while True:
   player = input("Choose rock, paper, or scissors: ").lower()
   games += 1
   computer = random.choice(choices)
   print("You chose:", player)
   print("Computer chose:", computer)
   if player not in choices:
       print("Invalid choice1")
       exit()
   if player == computer:
       print("It's a tie!")
   elif player == "rock" and computer == "scissors":
       print("You win!")
   elif player == "scissors" and computer == "paper":
       print("You win!")
   elif player == "paper" and computer == "rock":
       print("You win!")
   else:
       print("Computer win!")
   play_again = input("Play again?(Yes/No): ").lower()
   if play_again != "yes":
       break
print("Games played:", games)