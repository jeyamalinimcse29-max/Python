import random

print(" Welcome to Number Guessing Game ")
print("Select Difficulty Level:")
print("1. Easy (1 to 10, 5 chances)")
print("2. Medium (1 to 20, 4 chances)")
print("3. Hard (1 to 50, 3 chances)")

choice = int(input("Enter your choice (1/2/3): "))

# Difficulty settings
if choice == 1:
    number = random.randint(1, 10)
    attempts = 5
elif choice == 2:
    number = random.randint(1, 20)
    attempts = 4
elif choice == 3:
    number = random.randint(1, 50)
    attempts = 3
else:
    print("Invalid choice! Defaulting to Easy level.")
    number = random.randint(1, 10)
    attempts = 5

score = 0

print("\nGame Started! ")

for i in range(attempts):
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("🎉 Correct! You guessed the number!")
        score = attempts - i   # More score if guessed early
        break
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")

    print("Remaining attempts:", attempts - i - 1)

if score > 0:
    print(" Your Score:", score)
else:
    print(" You lost! The correct number was:", number)

print("Thank you for playing!")