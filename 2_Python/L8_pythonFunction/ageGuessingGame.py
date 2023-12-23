import random as r
ori_age = r.randint(15, 25)
flag = True


def age_guessing_fnc(gussed_age, originalage):
    if gussed_age > originalage:
        print("Too High")
    elif gussed_age < originalage:
        print("Too Low")
    else:
        return "CORRECT"


for i in range(5):
    guessing_age = input("---Guess my age--- You have " + str(5 - i) + " guesses left!\nYour Guess: ")
    if age_guessing_fnc(int(guessing_age), ori_age) == "CORRECT":
        print("YOU WON THE GAME!!!")
        flag = False
        break

if flag:
    print("OPPS! You Lose the game...")
