import random
import math

# Taking input for the lower bound
lower = int(input("Enter Lower bound: "))

# Taking input for the upper bound
upper = int(input("Enter Upper bound: "))

# Generating a random number between the lower and upper bounds
x = random.randint(lower, upper)
print("\n\tYou've only ", round(math.log(upper - lower + 1, 2)), " chances to guess the integer!\n")

# Initializing the number of guesses
count = 0

# Calculating the minimum number of guesses depends upon the range
while count < math.log(upper - lower + 1, 2):
    count += 1

    # Taking the guessing number as input
    guess = int(input("Guess a number: "))

    # Condition testing
    if x == guess:
        print("Congratulations! You guessed it correctly in ", count, " tries.")
        # Once guessed, the loop will break
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You guessed too high!")

# If the number of guesses exceeds the required limit, display this output
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")
