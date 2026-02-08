# import random
# import time

# while True:
#     choice=input('Roll the dice(y/n) ').lower()
#     if choice=='y':

#         print("rooling dice:....")
#         time.sleep(5)
#         dice1=random.randint(1,6)
      
#         print(f"{dice1}")
#     elif choice =='n':
#         print(f"thanks for playing")
#         break
#     else:
#         print(f"invalid choice")

import random
import time
import sys

while True:
    choice = input("Roll the dice (y/n): ").lower()
    if choice == 'y':
        print("Rolling dice...")

        # Dice rolling animation
        for _ in range(10):  # number of flashes
            dice_preview = random.randint(1, 6)
            sys.stdout.write(f"\r🎲 {dice_preview}")  # overwrite same line
            sys.stdout.flush()
            time.sleep(0.1)  # speed of animation (0.2 sec per frame)

        # Final dice result
        dice_result = random.randint(1, 6)
        sys.stdout.write(f"\r🎲 Dice shows: {dice_result}\n")
        

    elif choice == 'n':
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice, please enter y or n.")