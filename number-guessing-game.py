import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(" ")
print("Please select the difficulty level:")
print("1. Easy (10 chances)")
print("2. Medium (5 chances)")
print("3. Hard (3 chances)")

print(" ")
choice = input("Enter your choice: ")

if choice == '1':
    chances = 10
    print("\nYou selected Easy difficulty.")
elif choice == '2':
    chances = 5
    print(" ")
    print("Great! You have selected the Medium difficulty level.")
elif choice == '3':
    chances = 3
    print(" ")
    print("You selected Hard difficulty.")
else:
    print(" ")
    print("Invalid choice! Defaulting to Medium difficulty.")
    chances = 5

secret_number = random.randint(1, 100)
attempt = 0

print(" ")
print("Let's start the game!")

while attempt < chances:
    guess = int(input("\nEnter your guess: "))
    attempt += 1

    if guess < secret_number:
        print("Incorrect! The number is greater than", guess)
    elif guess > secret_number:
        print("Incorrect! The number is less than", guess)
    else:
        print(f"Congratulations! You guessed the correct number in {attempt} attempts.")
        break
else:
    print(f"\nSorry, you've used all {chances} attempts. The correct number was {secret_number}.")
