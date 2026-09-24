# Random_Number_Guessing_Game
# 🎯 Random Number Guessing Game

This is a simple Number Guessing Game made using Python.

In this game, the computer randomly generates a number between 1 and 10, and the player has 5 attempts to guess the correct number.

## 📌 How the Game Works

1. Python generates a random number between 1 and 10.
2. The player enters a number as their guess.
3. If the guessed number is smaller, the game tells the player to guess a bigger number.
4. If the guessed number is bigger, the game tells the player to guess a smaller number.
5. The player gets a maximum of 5 attempts.
6. If the player guesses correctly, they win.
7. If all 5 attempts are used, the correct number is displayed.

## 🛠️ Concepts Used

- Python `random` module
- Variables
- `while` loop
- `if` conditions
- User input
- `break` statement
- f-string

## 💻 Code

```python
import random

number = random.randint(1, 10)
attempt = 1

print("----Number Guessing Game !! ----")

while attempt <= 5:

    guess = int(input("\nGuess a Number Between 1 to 10 : "))

    if guess == number:
        print("Congratulations !! You guessed the correct number .")
        break

    if guess < number:
        print("It's Too Small Guys .. Guess a bigger number\n")

    if guess > number:
        print("It's Too Big Guys .. Guess a smaller number\n")

    attempt = attempt + 1

if guess != number:
    print("You lost the Game !! Better Luck Next Time .\n")
    print(f"The Right Number Was : {number}")
```

## ▶️ How to Run

Make sure Python is installed on your computer.

Clone the repository or download the Python file and run:

```bash
python number_guessing_game.py
```

## 🎮 Example

```text
----Number Guessing Game !! ----

Guess a Number Between 1 to 10 : 4
It's Too Small Guys .. Guess a bigger number

Guess a Number Between 1 to 10 : 8
It's Too Big Guys .. Guess a smaller number

Guess a Number Between 1 to 10 : 6
Congratulations !! You guessed the correct number .
```

## 🚀 What I Learned

While making this small project, I practiced how to:

- Generate random numbers in Python
- Take input from the user
- Use conditions for decision making
- Repeat code using loops
- Stop a loop using `break`
- Build simple game logic using Python

## 📚 About

This is a beginner Python project created while learning and practicing Python programming.

More improvements and Python projects will be added as I continue learning.