# This program demonstrates a guessing game
from random import  randint

# 1. Get user input
user_name = input('Input Name: ')
print('Hello there ' + user_name)

# 2.Using a while loop
# 3.Get user number
number = randint(10, 50)

counter = 0
while counter < 5:
    user_number = eval(input("Give me a number: "))




# 4.Generate a random number
# Check if user input is equal to generated number