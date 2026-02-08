dictr = {
    1: "ranjith",
    2: "ramesh",
    3: "ramu"
}

print("Search by:")
print("1 → ID")
print("2 → Name")

choice = input("Enter 1 or 2: ")

if choice == "1":
    v = int(input("Enter ID: "))
    if v in dictr:
        print(f"{v}, {dictr[v]} id and name : matched")
    else:
        print("ID not found")

elif choice == "2":
    s = input("Enter name: ")
    for key, value in dictr.items():
        if value == s:
            print(f"{key}, {value} id and name : matched")
            break
    else:
        print("Name not found")

else:
    print("Invalid choice")
