
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
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇



