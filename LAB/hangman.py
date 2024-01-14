name = input("What is your name? ") # Take the name of user
print("Hello, " + name, "It is time to play hangman!")
print("Start guessing...")
word = "CYSEC" #assign the sceret word
guesses = '' # creat an empty variable
turns = 10 # assign the number of turns
while turns > 0: # define loop
    failed = 0

    for char in word:
        if char in guesses:

            print(char)
        else:

            print("_")
            failed += 1

    if failed == 0:
        print("You found the keyword!")
        break #if completed break the game

    guess = input("guess a character:")

    guesses += guess

    if guess not in word:
        turns -= 1

        print("Wrong")

    print("You have", + turns, 'guesses left')

    if turns == 0:
        print("You lose")