import random

try:
    password = random.randint(100000, 999999)
    print("OTP:", password)

    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        data = input("Enter OTP: ")

        if not data.isdigit():
            print("Only numeric values are accepted. " )
            continue

        if int(data) == password:
            print("Thank you")
            break
        else:
            attempts += 1
            if attempts < max_attempts:
                print(f"Incorrect OTP. You have {max_attempts - attempts} attempt(s) left.")
            else:
                print("Too many incorrect attempts. Try again later.")

except Exception as e:
    print("An error occurred:", e)
