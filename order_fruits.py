available_fruits=["banana","apple","orange"]
print (f"We serve",",".join(available_fruits))
user_order= input("Enter your fruit: ").strip().lower()

bucket=[]
bucket.append(user_order)
for i in available_fruits:
    if user_order in available_fruits:
        addon = input("Do you want to add another fruit? (y/n): ").strip().lower()
        if addon == "y":
            while addon == "y":
                addon_fruit = input("Enter Addon fruit name: ").strip().lower()
                if addon_fruit in available_fruits:
                    bucket.append(addon_fruit)
                    print (f"Your fruit {bucket} is being packaging")
                    break
                elif addon_fruit not in available_fruits:
                    print(f"Sorry, {addon_fruit} is not available")
        elif addon == "n":
            print (f"Your order {bucket} is being packaging")
            break
    else:
        print (f"Sorry, {user_order} is not available")
        break



