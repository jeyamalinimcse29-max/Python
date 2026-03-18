import random

print("Rock Paper Scissors Game")

choices = ["rock", "paper", "scissors"]

user = input("Enter rock, paper, or scissors: ").lower()

computer = random.choice(choices)

print("Computer chose:", computer)

if user == computer:
    print("Result: Draw")

elif user == "rock" and computer == "scissors":
    print("Result: You Win")

elif user == "paper" and computer == "rock":
    print("Result: You Win")

elif user == "scissors" and computer == "paper":
    print("Result: You Win")

elif user in choices:
    print("Result: You Lose")

else:
    print("Invalid choice")