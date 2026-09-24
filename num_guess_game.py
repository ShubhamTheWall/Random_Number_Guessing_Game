import random

number = random.randint(1,10 )
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