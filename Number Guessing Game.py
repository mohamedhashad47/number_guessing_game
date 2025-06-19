# Number Guessing Game
from time import sleep
import random
import math
random_number=random.randint(1,100)
number_of_try=0
print("Welcome to the Number Guessing Game.")
sleep(1)
print("I'm thinking of a number between 1 and 100.")
sleep(1)
print("You have 5 chances to guess the correct number.")
sleep(1)
print("Please select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)")
print(random_number)
while True:
    try:
        difficulty_level=int(input("Enter your choice: "))
    except ValueError:
        print("please enter integer number")
        continue
    try:
        if difficulty_level==1:
            print("Great! You have selected the Easy difficulty level.")
            sleep(.5)
            print("Let's start the game!")
            while True:
                try:
                    your_guess=int(input("Enter your guess: "))
                    if number_of_try==10:
                        print("Hard luck,try again you lose")
                        exit(0)
                    if your_guess==random_number:
                        print(f"Congratulations! You guessed the correct number in {number_of_try} attempts.")
                        exit(0)
                    if your_guess>random_number:
                        print(f"Incorrect! The number is less than {your_guess}.")
                        number_of_try+=1
                        continue
                    if your_guess<random_number:
                        print(f"Incorrect! The number is greater than {your_guess}.")
                        number_of_try+=1
                        continue
                except ValueError:
                    print("please enter integer number")
                    continue
        elif difficulty_level==2:
            print("Great! You have selected the Medium difficulty level.")
            sleep(.5)
            print("Let's start the game!")
            while True:
                try:
                    your_guess=int(input("Enter your guess: "))
                    if number_of_try==5:
                        print("Hard luck,try again you lose")
                        exit(0)
                    if your_guess==random_number:
                        print(f"Congratulations! You guessed the correct number in {number_of_try} attempts.")
                        exit(0)
                    if your_guess>random_number:
                        print(f"Incorrect! The number is less than {your_guess}.")
                        number_of_try+=1
                        continue
                    if your_guess<random_number:
                        print(f"Incorrect! The number is greater than {your_guess}.")
                        number_of_try+=1
                        continue
                except ValueError:
                    print("please enter integer number")
                    continue
        elif difficulty_level==3:
            print("Great! You have selected the Hard difficulty level.")
            sleep(.5)
            print("Let's start the game!")
            while True:
                try:
                    your_guess=int(input("Enter your guess: "))
                    if number_of_try==3:
                        print("Hard luck,try again you lose")
                        exit(0)
                    if your_guess==random_number:
                        print(f"Congratulations! You guessed the correct number in {number_of_try} attempts.")
                        exit(0)
                    if your_guess>random_number:
                        print(f"Incorrect! The number is less than {your_guess}.")
                        number_of_try+=1
                        continue
                    if your_guess<random_number:
                        print(f"Incorrect! The number is greater than {your_guess}.")
                        number_of_try+=1
                        continue
                except ValueError:
                    print("please enter integer number")
                    continue
    except ValueError:
        print("please enter integer number between 1,2,3")
        continue