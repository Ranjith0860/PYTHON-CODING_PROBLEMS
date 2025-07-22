class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.\n")
        else:
            print("Invalid deposit amount.\n")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.\n")
        else:
            print("Insufficient balance or invalid amount.\n")

    def check_balance(self):
        print(f"Available balance: ₹{self.__balance}\n")

    def display_account_details(self):
        print("---- Account Details ----")
        print(f"Account Holder: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ₹{self.__balance}")
        print("--------------------------\n")


# ✅ Step 1: Safe input for name, account number, and balance
name = input("Enter your name: ")

while True:
    acc_no_input = input("Set your account number (numbers only): ")
    if acc_no_input.isdigit():
        acc_no = int(acc_no_input)
        break
    else:
        print("❌ Invalid input. Please enter numbers only.")

while True:
    balance_input = input("Enter initial deposit amount: ₹")
    if balance_input.isdigit():
        initial_balance = int(balance_input)
        break
    else:
        print("❌ Invalid input. Please enter numbers only.")

account = BankAccount(name, acc_no, initial_balance)

# ✅ Step 2: Ask user to verify account number before accessing menu
print("\n✅ Account created successfully!")
while True:
    entered_acc = input("🔐 Please verify your account number to continue: ")
    if entered_acc.isdigit():
        entered_acc_no = int(entered_acc)
        break
    else:
        print("❌ Invalid input. Please enter numbers only.")

# ✅ Step 3: Access menu only if account number matches
if entered_acc_no == account.account_number:
    while True:
        print("\n🏦 ---- Bank Menu ----")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Account Details")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            amt = input("Enter amount to deposit: ₹")
            if amt.isdigit():
                account.deposit(int(amt))
            else:
                print("❌ Invalid amount. Please enter a number.")

        elif choice == "2":
            amt = input("Enter amount to withdraw: ₹")
            if amt.isdigit():
                account.withdraw(int(amt))
            else:
                print("❌ Invalid amount. Please enter a number.")

        elif choice == "3":
            account.check_balance()

        elif choice == "4":
            account.display_account_details()

        elif choice == "5":
            print("Thank you for using the bank. Goodbye! 🏁")
            break

        else:
            print("❌ Invalid choice. Please try again.\n")

        # Ask if user wants to continue
        repeat = input("Do you want to continue? (yes/no): ").lower()
        if repeat != "yes":
            print("Exiting... Thank you for using our service.")
            break
else:
    print("❌ Account number mismatch. Access denied.")
