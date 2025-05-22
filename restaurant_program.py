username = input("Enter Username: ").strip().lower()
password = input("Enter Password: ")

if username == "user" and password == "1234":
    print(f"Restaurant Selection: ShopA or ShopB")
    restaurant = input("Enter Restaurant: ").strip().lower()
    if restaurant == "shopa":
        print("Menu: Salad Noodle,Plain Noodle,Soup")

        menu = input("Enter Menu: ").strip().lower()
        if menu == "salad noodle":
            print("Choose your taste: Spicy or Normal")
            taste = input("Enter Taste (Spicy or Normal): ").strip().lower()
            if taste == "spicy":
                print(f"Your Order: {menu} ({taste}) is preparing")
            elif taste == "normal":
                print(f"Your Order: {menu} ({taste}) is preparing")
            else:
                print(f"Please enter a valid taste choice")
        elif menu == "plain noodle":
            where = input("Where you gonna eat? Take Away or Eat Here?: ").strip().lower()
            if where == "take away":
                print(f"Your Order: {menu} is preparing and packaging to {where}")
            elif where == "eat here":
                print(f"Your Order: {menu} is preparing to {where}")
            else:
                print(f"Please enter a valid place to eat")
        elif menu == "soup":
            print ("Please choose your meal (Pork,Beef,Chicken)")
            meal = input("Enter Meal: ").strip().lower()
            if meal == "pork":
                taste = input("Enter Taste (Spicy or Normal): ").strip().lower()
                if taste == "spicy":
                    print(f"Your Order: {taste} {meal} {menu} is preparing!")
                elif taste == "normal":
                    print(f"Your Order: {taste} {meal} {menu} is preparing!")
                else:
                    print(f"Please enter a valid taste choice")
            elif meal == "beef":
                taste = input("Enter Taste (Spicy or Normal): ").strip().lower()
                if taste == "spicy":
                    print(f"Your Order: {taste} {meal} {menu} is preparing!")
                elif taste == "normal":
                    print(f"Your Order: {taste} {meal} {menu} is preparing!")
                else:
                    print(f"Please enter a valid taste choice")
            elif meal == "chicken":
                taste = input("Enter Taste (Spicy or Normal): ").strip().lower()
                if taste == "spicy":
                    print(f"Your Order: {taste} {meal} {menu} is preparing!")
                elif taste == "normal":
                    print(f"Your Order: {taste} {meal} {menu} is preparing!")
                else:
                    print(f"Please enter a valid taste choice")
            else:
                print(f"Please enter a valid Meal choice")
        else:
            print(f"Please enter a Menu")

    elif restaurant == "shopb":
        print("Menu: Hotpot,Curry,Drink")
        menu = input("Enter Menu: ").strip().lower()
        if menu == "hotpot":
            meal = input("Enter Meal(Chicken or Pork): ").strip().lower()
            if meal == "chicken":
                taste = input("Enter Taste (Spicy or Normal): ").strip().lower()
                if taste == "spicy":
                    print (f"OK! YOU Choose {taste} {menu} with {meal}.We are Preparing your order")
                elif taste == "normal":
                    print(f"OK! YOU Choose {taste} {menu} with {meal}.We are Preparing your order")
                else:
                    print(f"Please enter a valid taste choice")
            elif meal == "pork":
                taste = input("Enter Taste (Spicy or Normal): ").strip().lower()
                if taste == "spicy":
                    print (f"OK! YOU Choose {taste} {menu} with {meal}.We are Preparing your order")
                elif taste == "normal":
                    print(f"OK! YOU Choose {taste} {menu} with {meal}.We are Preparing your order")
                else:
                    print(f"Please enter a valid taste choice")
            else:
                print(f"Please enter a valid meal choice")
        elif menu == "curry":
            meal = input("Enter Meal(Chicken or Pork): ").strip().lower()
            if meal == "chicken":
                taste = input("Enter Taste (Spicy or Normal): ").strip().lower()
                if taste == "spicy":
                    print (f"OK! YOU Choose {taste} {menu} with {meal}.We are Preparing your order")
                elif taste == "normal":
                    print(f"OK! YOU Choose {taste} {menu} with {meal}.We are Preparing your order")
                else:
                    print(f"Please enter a valid taste choice")
            elif meal == "pork":
                taste = input("Enter Taste (Spicy or Normal): ").strip().lower()
                if taste == "spicy":
                    print (f"OK! YOU Choose {taste} {menu} with {meal}.We are Preparing your order")
                elif taste == "normal":
                    print(f"OK! YOU Choose {taste} {menu} with {meal}.We are Preparing your order")
                else:
                    print(f"Please enter a valid taste choice")
        elif menu == "drink":
            taste = input("Hot or Cold: ").strip().lower()
            if taste == "hot":
                print (f"Your Drink({taste}) is preparing")
            elif taste == "cold":
                print(f"Your Drink({taste}) is preparing")
            else:
                print(f"Please enter a valid Temperature choice")
        else:
            print("Please enter a valid menu")
    else:
        print(f"Please enter a valid restaurant choice")

