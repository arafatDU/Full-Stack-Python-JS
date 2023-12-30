print("===================================================================")
print("------------------------Number Guesser App-------------------------")
print("===================================================================\n")
print("                     1. Number Guesser Game\n                     2. Random Number Generator")
choice = int(input("Enter your choice: "))

if choice == 1:
    print("---------------------Number Guesser Game------------------------")
    import random
    import math

    # Taking Inputs
    lower = int(input("Enter Lower bound:- "))
    upper = int(input("Enter Upper bound:- "))

    # generating random number between
    # the lower and upper
    x = random.randint(lower, upper)
    print("\n\tYou've only ",
          round(math.log(upper - lower + 1, 2)),
          " chances to guess the integer!\n")

    # Initializing the number of guesses.
    count = 0

    # for calculation of minimum number of
    # guesses depends upon range
    while count < math.log(upper - lower + 1, 2):
        count += 1

        # taking guessing number as input
        guess = int(input("Guess a number:- "))

        # Condition testing
        if x == guess:
            print("Congratulations you did it in ",
                  count, " try")
            # Once guessed, loop will break
            break
        elif x > guess:
            print("You guessed too small!")
        elif x < guess:
            print("You Guessed too high!")

    # If Guessing is more than required guesses,
    # shows this output.
    if count >= math.log(upper - lower + 1, 2):
        print("\nThe number is %d" % x)
        print("\tBetter Luck Next time!")

elif choice == 2:
    print("---------------------Random Number Generator------------------------")
    import random
    import math

    # Taking Inputs
    lower = int(input("Enter Lower bound:- "))
    upper = int(input("Enter Upper bound:- "))
    while True:
        x = random.randint(lower, upper)
        print("=> {}".format(x))
        y = input("Do you want to Continue?(y/n): ")
        if y == 'y' or y == 'Y':
            continue
        else:
            break


else:
    print("Invalid Choice!")


