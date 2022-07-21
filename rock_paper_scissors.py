import random

print("Let's Play!!!")

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors']

while True:
    user_guess = input("Type Rock/Paper/Scissors or Q to quit: ").lower()

    if user_guess == 'q':
        break

    if user_guess not in options:
        print("Please enter valid answer!")
        continue

## rock: 1, paper: 2, scissors: 3

    computer_guess = options[random.randint(1,3)]
    print("Computer picked " + computer_guess + ".")

    if user_guess == "rock":
        if computer_guess == "rock":
            print("Its a tie!! Play again")
        elif computer_guess == "paper":
            print("Computer wins!!")
            computer_wins += 1
        else:
            print("You win!!")
            user_wins += 1

    if user_guess == "paper":
        if computer_guess == "paper":
            print("Its a tie!! Play again")
        elif computer_guess == "scissors":
            print("Computer wins!!")
            computer_wins += 1
        else:
            print("You win!!")
            user_wins += 1
        
    if user_guess == "scissors":
        if computer_guess == "scissors":
            print("Its a tie!! Play again")
        elif computer_guess == "rock":
            print("Computer wins!!")
            computer_wins += 1
        else:
            print("You win!!")
            user_wins += 1

print("You won " + str(user_wins) + " times and Computer won " + str(computer_wins) + " times.")
print("Goodbye!!")