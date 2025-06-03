import random
dice_number = (range(1,6))

#Computer Number
computer_num=random.choice(dice_number)
print (f"Computer number is {computer_num}")

#User Number
user_num=random.choice(dice_number)
print (f"User number is {user_num}")

if user_num == computer_num:
    print ("Match Draw")
elif user_num > computer_num:
    print ("You Win")
elif user_num < computer_num:
    print ("You Lose")
