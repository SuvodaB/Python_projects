import random

print("Welcome to the Game!!")

top_range = input("Type a number to be the upper limit of your guessing range: ")

if top_range.isdigit():
    top_range = int(top_range)

    if top_range<=0:
        print("Please type a number greater than 0 next time.")
        quit()
    
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0, top_range)
guesses = 0

while True:
    guesses += 1
    guess = input("Please guess a number: ")

    if guess.isdigit():
        guess = int(guess)

    else:
        print("Please type a number next time.")
        continue

    if guess == random_number:
        print("You got it!")
        break
    elif guess < random_number:
        print("You are below the number.")
    else:
        print("You are above the number.")

print("You got it in " + str(guesses) + " guesses")
