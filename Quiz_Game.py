print("Welcome to the Quiz Game!!")

#Ask for user input
interested = input("Do you want to play? ")

if interested.lower() != 'yes':
    quit()

print("Let's Play. Here's your quiz...")

right = 0

#First Question
answer1 = input("What is the capital of India? ")
if answer1.lower() == "delhi" or answer1.lower() == "new delhi":
    print("That's Correct!")
    right+=1
else:
    print("Oopsy!!")

#Second Question
answer2 = str(input("Who is the Prime Minister of India? "))
if answer2.lower() == "narendra modi":
    print("That's Correct!")
    right+=1
else:
    print("Oopsy!!")

#Third Question
answer3 = str(input("What was Ross's favourite line? "))
if answer3.lower() == "we were on a break":
    print("That's Correct!")
    right+=1
else:
    print("Oopsy!!")

#Fourth Question
answer4 = str(input("Who stole Monica's thunder? "))
if answer4.lower() == "rachel":
    print("That's Correct!")
    right+=1
else:
    print("Oopsy!!")

#Fifth Question
answer5 = str(input("What is the full form of np? "))
if answer5.lower() == "no problem":
    print("That's Correct!")
    right+=1
else:
    print("Oopsy!!")

print("Congrats!! You are done. Look out for your score below!")
print("You have got {} questions correct. ".format(right))
print("You got " + str((right/5) * 100) + "%.")