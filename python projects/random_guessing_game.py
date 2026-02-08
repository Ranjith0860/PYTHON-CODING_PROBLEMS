import random

playing=True
choices=(1,5,3,6,7,9)
guess_number=random.choice(choices)
while playing:
    try:
        guess=int(input("enter your guess number:1to10"))
        if guess < guess_number:
            print("you are low")
        elif guess > guess_number:
            print("you are too high")
        else :
            print(f"your gussed correct number {guess_number} thaks for playing ")
            break


    except ValueError:
        print("enter correct value")


    

