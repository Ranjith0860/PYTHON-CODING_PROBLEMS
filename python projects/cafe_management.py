# Menu items and prices
orders = {
    'pizza': 50,
    'coffee': 60,
    'burger': 90,
    'milkshake': 120,
    'shawarma': 210
}

# Matching emojis for each item
emojis = {
    'pizza': '🍕',
    'coffee': '☕',
    
    'milkshake' : '🥤',
    'shawarma': '🌯',
    'burger' : '🌯'
    
}

while True:
    print("\nHERE IS THE MENU:")

    # Use FOR loop to print menu
    for item in orders:
        print(f" {item.capitalize()}, {emojis[item]} : ₹{orders[item]}")

    total = 0
    user_order = input("\nChoose your order from the menu :").lower()

    if user_order in orders:
        total += orders[user_order]
        print(f"Your order '{user_order} {emojis[user_order]}' is placed! 🎉")
    else:
        print("Item not available. Please enter an available order. ⚠️")
        continue

    another_order = input("\nDo you want another order? (yes) or \npress any key to (no): ").lower()

    if another_order == 'yes':
        print("\nMENU AGAIN:")

        # Again FOR loop to show menu
        for item in orders:
            print(f" {item.capitalize()} {emojis[item]} : ₹{orders[item]}")

        item_2 = input("\nEnter 2nd item: ").lower()

        if item_2 in orders:
            total += orders[item_2]
            print(f"The 2nd item '{item_2} {emojis[item_2]}' has been placed! ✅")
            print(f"Your orders are: {user_order} {emojis[user_order]}, {item_2} {emojis[item_2]}")
        else:
            print(f"'{item_2}' not available. ❌")

        break

    else:
        print("\nThanks! Please rate us 🌟")
        break

print(f"\nTotal bill: ₹{total} Thank you👍")
