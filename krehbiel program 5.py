items = {
    1: 1.50, 2: 4.50, 3: 0.50, 4: 0.75, 5: 1.00
}

def calculate_total_purchase():
    total = 0.0
    print("                     Welcome to our Store! \n"
          "   Please select the number relating to the item you would like\n"
          "   1 - Hotdog $1.50 | 2 - Chilidog $4.50 | 3 - Cheese $0.50 | "
          "   4 - Peppers $0.75 | 5 - Grilled Onions $1.00 \n"
          "   Type 'done' to finish your order.")

    while True:
        user_input = input("Enter a number (or type 'done' to finish): ")

        if user_input.lower() == "done":
            break

        try:
            item_number = int(user_input)
            if item_number in items:
                total += items[item_number]
            else:
                print("Invalid choice, try again.")
        except ValueError:
            print("Invalid input, please enter a number or 'done'.")

    return total

# Mainline
total_price = calculate_total_purchase()
print(f"Your total is ${total_price:.2f}")