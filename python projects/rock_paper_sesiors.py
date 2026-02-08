# import random,input,computer output r=r,p=p,s=s is tie

import random as R

choices=('r','p','s')

while True:
    user_choice=input("eneter rock,paper,siscors as (r/p/s): ").lower()

    if user_choice not in choices:
        print("invaild choice enter correct option(r/p/s): ")
        continue

    computer_choice=R.choice(choices)
    print("computer choice",computer_choice)
    print("your choice",user_choice)

    if user_choice == computer_choice:
        print("its a tie😁")

    elif(user_choice=='r' and computer_choice=='s') or\
        (user_choice=='s' and computer_choice=='p') or\
        (user_choice=='p' and computer_choice=='r'):
        print("you win 👌")
    else:
        print("you lot better luck next time😊")

    continue_game=input("enter a choice if you want to play again (y/n)").lower()

    if continue_game not in('y','n'):
        print('invaild choice enter correct option ')
        continue_game=input("enter a choice if you want to play again (y/n)").lower()
            
    if continue_game=='n':
        print("thank for playing❤️")
        break




