# NUMBER GUESSING GAME
# Computer picks a random number between 1–100
# User gets 7 attempts
# Bonus: best score tracking + hint when close

import random

best_score = None   # to store minimum attempts used

while True:
    number = random.randint(1, 100)
    attempts = 7
    used = 0

    print("\nI picked a number between 1 and 100.")
    print("You have 7 attempts.")

    while attempts > 0:
        guess = int(input("Enter your guess: "))
        used += 1
        attempts -= 1

        if guess == number:
            print("Correct! You guessed it in", used, "attempts")

            # bonus: track best score
            if best_score is None or used < best_score:
                best_score = used
                print(" New best score:", best_score)

            break

        elif guess > number:
            print("Too high!")
        else:
            print("Too low!")

        # bonus hint when close
        if abs(guess - number) <= 5:
            print("Hint: You are VERY close!")

        if attempts > 0:
            print("Attempts left:", attempts)

    else:
        print(" You failed. The number was:", number)

    # play again option
    again = input("Play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing!")
        break