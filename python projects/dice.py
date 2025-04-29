import random
playing=True
while playing:
    choice=input("Enter the choice(y/n)").lower()
    if choice == 'y':
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
        print(f"your dice is rolled :{dice1},{dice2}")
    elif choice == 'n':
        print(f"thanks for playing")
        break
    else:
        print("invalid choice")

