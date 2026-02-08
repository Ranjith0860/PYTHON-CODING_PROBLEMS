import random

class Bank():
    Bname = "iRK Bank"
    clients = []

    def updateUser(self, client):
        self.clients.append(client)

    def authenticate(self, name, account_number, password):
        auth = False
        for i in self.clients:
            if (i.account["name"] == name and
                i.account["accno"] == account_number and
                i.account["password"] == password):
                auth = True
                return i
        print("Wrong credentials\n enter correct name or mail or password")
        return False

class Client():
    account = {}

    def __init__(self, name, deposit, password):
        self.account["name"] = name
        self.account["deposit"] = deposit
        self.account["accno"] = random.randint(100000, 999999)
        self.account["password"] = password
        print(f"Your account has been created, account number is: {self.account['accno']}")

    def deposit(self, amnt):
        self.account["deposit"] += amnt
        print("Deposit successful")

    def withdraw(self, amnt):
        if self.account["deposit"] >= amnt:
            self.account["deposit"] -= amnt
            print("Withdrawal successful")
        else:
            print("Insufficient funds")

    def check(self):
        print(f"Balance: {self.account['deposit']} rupees")

def main():
    bank = Bank()
    print(f"Hello and welcome to {bank.Bname}")
    flag = True
    while flag:
        print("""What would you like to do:
                1.) Create a new account
                2.) Inquire existing account
                3.) Exit""")
        choice = int(input("Press 1, 2, or 3: "))
        if choice == 1:
            name = input("Enter name: ")
            deposit = int(input("Enter deposit amount: "))
            password = input("Enter password: ")
            client = Client(name, deposit, password)
            bank.updateUser(client)
        elif choice == 2:
            name = input("Enter name: ")
            account_number = int(input("Enter account number: "))
            password = input("Enter password: ")
            current_client = bank.authenticate(name, account_number, password)
            if current_client:
                print("""What would you like to do:
                        1.) Deposit
                        2.) Withdraw
                        3.) Check balance
                        4.) Exit""")
                choice = int(input("Press 1, 2, 3, or 4: "))
                if choice == 1:
                    amount = int(input("Enter deposit amount: "))
                    current_client.deposit(amount)
                elif choice == 2:
                    amount = int(input("Enter withdrawal amount: "))
                    current_client.withdraw(amount)
                elif choice == 3:
                    current_client.check()
                else:
                    print("Thank you for visiting")
            else:
                print("Authentication failed")
        else:
            flag = False
    print("Thank you")
    return "Bye"

if __name__ == "__main__":
    main()