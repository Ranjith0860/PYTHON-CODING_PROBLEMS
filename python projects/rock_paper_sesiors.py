import random

choices=('r','p','s')
while True:
    user_choice = input(f"rock,paper,siscors (r/p/s):").lower()
    if user_choice not in choices:
        print("invailid choice please enter a  valid choice: r/p/s")
        continue
   
   
    
    computer_choice=random.choice(choices)

    print(f"your choice: {user_choice}")
    print(f'computer choice {computer_choice}')
    if user_choice == computer_choice:
        print("tie")
       
    elif (user_choice=='r' and computer_choice=='s' or user_choice =='s' 
          and computer_choice =='p' or user_choice =='p' 
          and computer_choice =='r'): 
        print("you win")
    else:
        print("you lose")
    z=('y','n')

    continue_1=input(f"do want to play again (y/n) :").lower()
    if continue_1 not in  z:
         print("enter a char y/n: ")
    elif continue_1=='n':
        break

