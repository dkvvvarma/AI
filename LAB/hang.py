
name = input("What is your name? ")

print("Hello, " + name, "It is time to play hangman!")

print("Start guessing...")

word = "secret"

guesses = ''

turns = 10

while turns > 0:

    failed = 0

    for char in word:
        if char in guesses:

            print(char)
        else:

            print("_")
            failed += 1

    if failed == 0:
        print("You won!")
        break

    guess = input("guess a character:")

    guesses += guess

    if guess not in word:
        turns -= 1

        print("Wrong")

    print("You have", + turns, 'more guesses')

    if turns == 0:
        print("You lose")
