import random

random_number = random.randint(1, 10)

while True:
    user_input = input("Guess the number (between 1 and 10): ")

    if int(user_input) == random_number:
        print(f"Congratulations! You guessed the correct number: {random_number}")
        break  
    else:
        print("Wrong guess, try again!") 
