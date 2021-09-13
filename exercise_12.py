# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
import random
random_number = random.randint(1,9)
guess = 0
count = 0
while guess != 'number' and guess != 'exit':
    guess = input("What is your guess ?")
    
    if guess == 'exit':
        break;
    
    guess = int(guess)
    count += 1
    
    if guess < random_number:
        print("Your guess is too low")
    
    elif guess > random_number:
        print("Your guess is too high")
    else:
        print("You have got the correct number. It only took you", count, " tries")
        break
