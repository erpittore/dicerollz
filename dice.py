from random import randint

def roll_dice():
    print(f"Number is: {randint(1,8)}")

roll_dice()   

roll_amount = 5 
for number in range(roll_amount):
    roll_dice()