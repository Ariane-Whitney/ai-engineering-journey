# Day 3 - Number Guessing Game (CLI Version)
# Concepts: Loops, Conditionals, Random, Input Validation
import random

secret_number = random.randint(1, 10)

attempts = 0
max_attempts = 5

print("🎮 Welcome to the Number Guessing Game!")
print("You have 5 attempts to guess a number between 1 and 10.\n")

while attempts < max_attempts:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < 1 or guess > 10:
            print("⚠ Please enter a number between 1 and 10.\n")

        elif guess < secret_number:
            print("📉 Too low! Try again.\n")

        elif guess > secret_number:
            print("📈 Too high! Try again.\n")

        else:
            print(f"🎉 Congratulations! You guessed the number in {attempts} attempts!")
            break

    except ValueError:
        print("❌ Invalid input. Please enter a valid number.\n")

# If user used all attempts and didn't guess correctly
if attempts == max_attempts and guess != secret_number:
    print(f"💀 Game Over! The correct number was {secret_number}.")
