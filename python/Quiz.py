
# Quiz_6

# Day 1 - Python Print Function
# The function is declared like this:
# print('what to print')

# print("Day 1 - Python Print Function")
# print("The function is declared like this:")
# print("print('what to print')")


# Quiz_8

# Day 1 - String Manipulation
# String Concatenation is done with the "+" sign.
# e.g. print("Hello " + "world")
# New lines can be created with a backslash and n.

# print("Day 1 - String Manipulation")
# print('String Concatenation is done with the "+" sign.')
# print('e.g. print("Hello " + "world")')
# print("New lines can be created with a backslash and n.")

# Quiz_10

# print(len(input("What is your name? ")))

# Quiz_12

# 🚨 Don't change the code below 👇
# a = input("a: ")
# b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
# c = a
# a = b
# b = c
#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
# print("a: " + a)
# print("b: " + b)


# Quiz_14

# print("Welcome to the Band Name Generator.")
# city = input("What's name of the city you grew up in?\n")
# name = input("What is your name?\n")

# print("hello " + name + "." + " I'm from " + city + ".")

# Quiz_19

# number = input()
# first_num = number[0]
# second_num = number[1]
# result = int(first_num) + int(second_num)
# print(result)


# Quiz_21

# 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# bmi = int(weight) / (float(height)** 2)
# print(round(bmi))


# Quiz_23

# age = input("What is your current age? ")

# days = (90 * 365) - (int(age) * 365)
# weeks = (90 * 52) - (int(age) * 52)
# months = (90 * 12) - (int(age) * 12)

# print(f"You have {days} days, {weeks} weeks and {months} months left")


# Project_24 - Tip Calculator

# print("Welcome to the tip calculator")
# bill = input("What was the total bill?  ")
# percent = input("What percentage tip would you like to give? 10, 12, or 15?  ")
# people_count = input("How many people to split the bill?  ")

# result = float(bill) * ((float(percent) / 100) + 1)
# result_percent = round(result, 2)
# pay =  round(result_percent / int(people_count), 2)
# pay = "{:.2f}".format(pay)

# print(f"Each person should pay: ${pay}")


# Quiz_28

# 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# if number % 2 == 0:
  # print("This is even Number.")
# else:
  # print("This is odd Number.")


# Quiz_30

# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg:  "))

# bmi = weight / height**2
# bmi_result = round(bmi, 2)
# if bmi_result < 18.5:
#   print(f"You are {bmi_result}. It is underweight")
# elif bmi_result < 25:
#   print(f"You are {bmi_result}. It is normal weight")
# elif bmi_result < 30:
#   print(f"You are {bmi_result}. It is overweight")
# elif bmi_result < 35:
#   print(f"You are {bmi_result}. It is obese")
# else:
#   print(f"Above 35 is elinically obese.")


# Quiz_31

# year = int(input("which year do you want yo check?"))

# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#   print("leap")
# else:
#   print("Not Leap")

# Quiz_33

# 🚨 Don't change the code below 👇
# from re import M


# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# pay = 0
# if size == "S":
#   pay = 15
# elif size == "M":
#   pay = 20
# else:
#   pay = 25

# if add_pepperoni == "Y":
#   if size == "S":
#     pay += 2
#   else:
#     pay += 3

# if extra_cheese == "Y":
#   pay += 1
    
# print(f"Your final bill is: ${pay}")


# Quiz_35

# 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# name = name1.lower() + name2.lower()

# count_t = name.count("t")
# count_r = name.count('r')
# count_u = name.count('u')
# count_e = name.count('e')

# count_l = name.count('l')
# count_o = name.count('o')
# count_v = name.count('v')

# count_true = count_t + count_r + count_u + count_e
# count_love = count_l + count_o + count_v + count_e

# love_score = str(count_true) + str(count_love)

# if int(love_score) < 10 or int(love_score) > 90:
#   print(f"Your score is {love_score}, you go together like coke and mentos.")
# elif 40 <= int(love_score) <= 50:
#   print(f"Your score is {love_score}, you are alright together.")
# else:
#   print(f"Your score is {love_score}")


# Quiz_36

# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

# first_answer = input("'You're at a crossroad. Where do you want to go? Type 'left' or 'right'")
# fl_answer = first_answer.lower()

# if fl_answer == "left":
#   second_answer = input("'You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.'")
#   sl_answer = second_answer.lower()
#   if sl_answer == "swim":
#     third_answer = input('"You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?"')
#     tl_answer = third_answer.lower()
#     if tl_answer == "yellow":
#       print('"You found the treasure! You Win!"')
#     else:
#       print('"It`s a room full of fire. Game Over."')
#   else:
#     print('"You get attacked by an angry trout. Game Over."')
# else:
#   print("Your Die!")

# Quiz_40

# import random

# head = "Heads"
# tail = "Tails"

# random_text = random.randint(0, 1)
# if random_text == 0:
#   print(head)
# else:
#   print(tail)

#quiz_42

# Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(",")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# import random

# names_number = len(names)
# pay_member = random.randint(0, names_number - 1)
# buya = names[pay_member]

# print(f"{buya} pay today lunch, Thank you!")


# Quiz_44

# 🚨 Don't change the code below 👇
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# position_list = list(position)

# i = 1

# while i < 4:
#   if position_list[0] == f"{i}" and position_list[1] == "1":
#     map[0][i-1] = "X"
#   elif position_list[0] == f"{i}" and position_list[1] == "2":
#     map[1][i-1] = "X"
#   elif position_list[0] == f"{i}" and position_list[1] == "3":
#     map[2][i-1] = "X"
#   i += 1

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")


# Quiz_45

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

#Write your code below this line 👇

# import random

# choose = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
# print(choose)

# if choose == "0":
#   print(rock)
# elif choose == "1":
#   print(paper)
# elif choose == "2":
#   print(scissors)
# else:
#   print("wrong number.")

# print("Computer chose :")

# list = [rock, paper, scissors]

# computer_chose = random.choice(list)
# print(computer_chose)

# choose_number = int(choose)

# if choose_number == 0 and computer_chose == rock:
#   print("Draw.")
# elif choose_number == 0 and computer_chose == paper:
#   print("You lose.")
# elif choose_number == 0 and computer_chose == scissors:
#   print("You win!")
# elif choose_number == 1 and computer_chose == rock:
#   print("You win!")
# elif choose_number == 1 and computer_chose == paper:
#   print("Draw.")
# elif choose_number == 1 and computer_chose == scissors:
#   print("You lose.")
# elif choose_number == 2 and computer_chose == rock:
#   print("You lose.")
# elif choose_number == 2 and computer_chose == paper:
#   print("You win!")
# elif choose_number == 2 and computer_chose == scissors:
#   print("Draw.")
# elif choose_number != 0 or choose_number != 1 or choose_number != 2:
#   print("You wrong number, lose.")


# ======== other case =========================


# import random 

# list = [rock, paper, scissors]
# choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))


# if choose < 0 or choose >= 3:
#   print("wrong number, you lose")
# else:
#   print(list[choose])

#   computer_chose = random.randint(0, 2)
#   print(f"computer chose is :")
#   print(list[computer_chose])

#   if choose == 2 and computer_chose == 0:
#     print("you lose")
#   elif choose > computer_chose:
#     print("you win!")
#   elif choose == 0 and computer_chose == 2:
#     print("you win")
#   elif choose < computer_chose:
#     print("you lose")
#   elif choose == computer_chose:
#     print("draw")


# quiz_49

# 🚨 Don't change the code below 👇
# from turtle import heading


# student_heights = input("Input a list of student heights ").split()

# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# height = 0
# number = 0

# for student in student_heights:
#   height += student
#   number += 1

# total_height = height / number
# print(total_height)
  


