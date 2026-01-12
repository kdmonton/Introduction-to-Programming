items = {
    "A1": {"name": "Chips(a)", "price": 40.25, "stock": 8},                           #Item prices and stocks 
    "A2": {"name": "Biscuit", "price": 35.75, "stock": 8},
    "A3": {"name": "Candies", "price": 20.50, "stock": 8},

    "B1": {"name": "Water", "price": 15, "stock": 8},
    "B2": {"name": "Soda", "price": 50.25, "stock": 8},
    "B3": {"name": "Chips(b)", "price": 45, "stock": 8},
}

accepted_money = [0.25, 0.50, 5, 10, 20, 50, 100, 200, 500, 1000]                    #Accepted coins and bills in AED
change = [1000, 500, 200, 100, 50, 20, 10, 5, 0.50, 0.25]                            #Biggest to smallest for it to make the biggest change to give as possible


def give_change(amount):                                                             #This function breaks down the remaining balance into bills and coins
    if amount <= 0:
        print("No balance")
        return
    print("\nChange given:")
    for c in change:
        count = int(amount // c)                                                     #How many of this bill/coin
        if count > 0:
            print(f"AED {c} x {count}")
            amount = round(amount - (c * count), 2)


while True:
    cart = []                                                                       #Stores purchased items
    balance = 0.0                                                                   #Money available to spend
    total_inserted = 0.0                                                            #Total money inserted (for refunds)

    print("\nVENDING MACHINE")                                                      #This is how the user should see the vedning machine if it was physically there
    print("A1  A2  A3")
    print("B1  B2  B3\n")

    for code, item in items.items():                                                #Show all items with prices and stock
        print(f"{code}: {item['name']} - {item['price']}AED (Stock: {item['stock']})")

    # MONEY INSERTION
    while True:
        money_input = input("\nInsert money (or 'lock', 'cancel'): ").lower()

        if money_input == "cancel":                                                 #Cancel = return money
            give_change(balance)
            balance = 0
            continue

        if money_input == "lock":                                                   #Lock = stop inserting money and go to item selection
            if balance <= 0:
                print("Insert money first")
                continue
            break

        try:                                                                        #Check if input is a number
            money = float(money_input)
        except ValueError:
            print("Invalid input")
            continue

        if money in accepted_money:                                                 #Accept money only if it is valid (only in the accepted_money)
            balance += money
            total_inserted += money
            print(f"Balance: {balance} AED")
        else:
            print("Invalid money")

    # ITEM SELECTION
    while True:
        print(f"\nCurrent balance: {balance} AED")
        choice = input("Select item (done / exit): ").upper()

        if choice == "DONE":                                                        #DONE = finish purchase and dispense items
            print("\nPurchase completed")
            for name, price in cart:
                print(f"Dispensing {name}")
            give_change(balance)
            break

        if choice == "EXIT":                                                        #EXIT = cancel everything and refund full money
            print("Transaction cancelled")
            give_change(total_inserted)
            exit()

        if choice not in items:                                                     #Invalid code check
            print("Invalid selection")
            continue

        item = items[choice]

        if item["stock"] <= 0:                                                       # Stock check
            print("Item out of stock")
            continue

        if balance < item["price"]:                                                  # Balance check
            print("Not enough balance")
            continue

        # BUY ITEM
        balance -= item["price"]
        item["stock"] -= 1
        cart.append((item["name"], item["price"]))

        print(f"Added {item['name']} to cart")
        print(f"Remaining balance: {balance} AED")

        # RECOMMENDATION SYSTEM (WITH STOCK CHECK)
        if item["name"] in ["Water", "Soda"]:
            rec_code = "A1"                                                         #This recommend Chips(a)
        elif "Chips" in item["name"]:
            rec_code = "B1"
        elif item["name"] == "Biscuit":
            rec_code = "B1"                                                        #This recommends Water
        elif item["name"] == "Candies":
            rec_code = "B1"
        else:
            continue

        rec_item = items[rec_code]

        if rec_item["stock"] > 0 and balance >= rec_item["price"]:                  #Recommend only if item is in stock and affordable
            ans = input(
                f"Would you like to purchase {rec_item['name']} for {rec_item['price']}AED? (yes/no): "
            ).lower()

            if ans == "yes":
                balance -= rec_item["price"]
                rec_item["stock"] -= 1
                cart.append((rec_item["name"], rec_item["price"]))
                print(f"Added {rec_item['name']} to cart")
                print(f"Remaining balance: {balance} AED")
