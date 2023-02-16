# This program demonstrates a guessing game
from random import randint

# 1. Get user input
user_name = input('Input Name: ')
print('Hello there ' + user_name)

# 2.Using a while loop
# 3.Get user number
# 4.Generate a random number
random_number = randint(10, 50)

counter = 0
while counter < 5:
    user_number = eval(input("Give me a number: "))
    counter += 1

    if user_number < random_number:
        print("HA! Too low!!")
    elif user_number > random_number:
        print("HE..HE..HE! Too high Fool!!")
    elif user_number == random_number:
        break

if user_number == random_number:
    print("Ok,FINE! You win")
else:
    print("YOU DUMB BRO! you lose")
    print("The answer is " + str(random_number))
# Check if user input is equal to generated number
