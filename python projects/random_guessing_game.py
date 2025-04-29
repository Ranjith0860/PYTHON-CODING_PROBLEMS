import random

playing=True
guess_number=random.randint(1,100)
while playing:
    try:
        guess=int(input("enter your guess number"))
        if guess < guess_number:
            print("you are low")
        elif guess > guess_number:
            print("you are too high")
        else :
            print(f"your gussed correct number {guess_number} thaks for playing ")
            break


    except ValueError:
        print("enter correct value")


    

