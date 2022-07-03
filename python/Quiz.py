
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
  

# quiz_50

#  # 🚨 Don't change the code below 👇
# from turtle import hideturtle


# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# high_score = 0

# for score in student_scores:
#   if score > high_score:
#     high_score = score

# print(f"The highest score in the class is: {high_score}")


# quiz_52

# from re import I

# number = 0

# for i in range(1, 101):
#   if i % 2 == 0:
#     number += i
# print(number)

# quiz_53

# for i in range(1, 101):
#   if i % 3 == 0 and i % 5 == 0:
#     print("FizzBuzz!")
#   elif i % 3 == 0:
#     print("Fizz")
#   elif i % 5 == 0:
#     print("Buzz")
#   else:
#     print(i)

# quiz_54

#Password Generator Project
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# password = ""

# for i in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for i in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for i in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# list = list(password)
# random.shuffle(list)

# result = ""
# for password in list:
#   result += password

# print(result)

# result = ""
# for password in password_r:
#   result += password

# print(result)

# passw = random.shuffle(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


# 63_ Reeborg's worlds

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while front_is_clear():
#     move()
# turn_left()
    
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()


# Quiz 67

#Step 1 

# word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# import random
# chosen_word = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# guess = input("Guess a letter: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the leters in the chosen_word.
# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")


# Quiz 69
#Step 2

# import random
# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

# words = []
# word_length = len(chosen_word)

# for word in range(word_length):
  # words += "_"

# guess = input("Guess a letter: ").lower()

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

# for position in range(word_length):
  # letter = chosen_word[position]
  # if letter == guess:
    # words[position] = letter


#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
# print(words)


# Quiz_71

#Step 3

# import random
# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
# display = []
# for _ in range(word_length):
    # display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

# while True:
  # guess = input("Guess a letter: ").lower()

#Check guessed letter
  # for position in range(word_length):
    # letter = chosen_word[position]
    # if letter == guess:
      # display[position] = letter
  # print(display)
  # if "_" in display:
    # continue
  # else:
    # print("you win")
    # break

# Quiz_73

#Step 4
# import random

# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']

# end_of_game = False
# word_list = ["ardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
# lives = 6

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
# display = []
# for _ in range(word_length):
    # display += "_"

# while not end_of_game:
    # guess = input("Guess a letter: ").lower()

    #Check guessed letter
    # for position in range(word_length):
        # letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        # if letter == guess:
            # display[position] = letter

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    # if guess not in chosen_word:
      # lives -= 1
      # if lives == 0:
        # end_of_game = True
        # print("You lose.")
    
    #Join all the elements in the list and turn it into a String.
    # print(f"{' '.join(display)}")

    #Check if user has got all letters.
    # if "_" not in display:
        # end_of_game = True
        # print("You win.")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    # print(stages[lives])


# quiz_75

#Step 5

# import random
# from hangman_art import stages, logo
# from hangman_word import word_list

# #TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
# #Delete this line: word_list = ["ardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)

# end_of_game = False
# lives = 6

# #TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
# print(logo)

# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# #Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"

# while not end_of_game:
#     guess = input("Guess a letter: ").lower()

#     #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
#     if guess in display:
#           print("You already guessed.")
  
#     #Check guessed letter
#     for position in range(word_length):
#         letter = chosen_word[position]
#         # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#         if letter == guess:
#             display[position] = letter

#     #Check if user is wrong.
#     if guess not in chosen_word:
#         #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
#         lives -= 1
#         print("it's not in the word")
#         if lives == 0:
#             end_of_game = True
#             print("You lose.")

#     #Join all the elements in the list and turn it into a String.
#     print(f"{' '.join(display)}")

#     #Check if user has got all letters.
#     if "_" not in display:
#         end_of_game = True
#         print("You win.")

#     #TODO-2: - Import the stages from hangman_art.py and make this error go away.
#     print(stages[lives])

# Quiz_81
# import math

# def paint_calc(height, width, cover):
#   can = (test_h * test_w) / coverage
#   cans = math.ceil(can)
#   print(f"You'll need {cans} cans of paint.")


# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)



# Quiz _ 82   소수 판별 알고리즘

#Write your code below this line 👇

# def prime_checker(number):
#   is_prime = True
#   for i in range(2, number):
#     if number % i == 0:
#       is_prime = False
  
#   if is_prime == True:
#       print("It's a prime number.")
#   else:
#       print("It's not a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
# n = int(input("Check this number: "))
# prime_checker(number=n)


#Quiz_83  

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# def encrypt(plain_text, shift_amount):
#   cipher_text = ""
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     new_letter = alphabet[new_position]
#     cipher_text += new_letter
#   print(f"The encoded text is {cipher_text}")

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
# encrypt(plain_text=text, shift_amount=shift)


#Quiz_84

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def caesar(start_text, shift_amount, cipher_direction):
#   end_text = ""
#   if cipher_direction == "decode":
#       shift_amount *= -1
#   for char in start_text:
#     if char in alphabet:
#       position = alphabet.index(char)
#       new_position = position + shift_amount
#       end_text += alphabet[new_position]
#     else:
#       end_text += char
#   print(f"Here;s the {direction}d result: {end_text}")

# should_continue = True

# while should_continue:
#   direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#   text = input("Type your message:\n").lower()
#   shift = int(input("Type the shift number:\n"))
#   # 26보다 큰 수를 입력했을 때 에러 방지 (나눈 후 나머지 값이 shift 값이 되도록 함)
#   shift = shift % 26
#   caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

#   result = input("Type yes or no.")
#   if result == "no":
#     should_continue = False
#     print("Good bye")


# Quiz _ 90

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# #TODO-1: Create an empty dictionary called student_grades.
# student_grade = {}

# #TODO-2: Write your code below to add the grades to student_grades.👇
# for student in student_scores:
#   score = student_scores[student]
#   if score > 90:
#     student_grade[student] = "수"
#   elif score > 80:
#     student_grade[student] = "우"
#   elif score > 70:
#     student_grade[student] = "미"
#   else:
#     student_grade[student] = "Fail"

# # 🚨 Don't change the code below 👇
# print(student_grade)


# Quiz_92
# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above

# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇

# def add_new_country(country, time, cities):
#   new_country = {}
#   new_country["country"] = country
#   new_country["visits"] = time
#   new_country["cities"] = cities
#   travel_log.append(new_country)
  
# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)


# Quiz_92
# order = {
#     "starter": {1: "Salad", 2: "Soup"},
#     "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
#     "dessert": {1: ["Ice Cream"], 2: []},
# }

# print(order["main"][2][0])


#Quiz_94

# import os
# clear = lambda: os.system('cls')

# pay = {}
# other_person = True

# def highest_payer(pay):
#   highest_bid = 0
#   winner = ""
#   for one in pay:
#     bid = pay[one]
#     if bid > highest_bid:
#       highest_bid = bid
#       winner = one
#   print(f"The winner is ${winner} with a bid of ${highest_bid}")

# while other_person:
#   name = input("What is your name?: ")
#   bid = input("What is your bid?: $")

#   pay[name] = int(bid)

#   answer = input("Other person? (yes or no) : ")
#   if answer == "no":
#     other_person = False
#     highest_payer(pay)
#   else:
#     clear()


# Quiz_99

# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# def days_in_month(year, month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
#   if is_leap(year) and month ==2:
#     return 29
#   return month_days[month-1] 
  
  
# #🚨 Do NOT change any of the code below 
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)



# def outer_function(a, b):
#     def inner_function(c, d):
#         return c + d
#     return inner_function(a, b)
 
# result = outer_function(5, 10)
# print(result)


#Quiz_101

#Calculator

# def add(n1, n2):
#   return n1 + n2

# def minus(n1, n2):
#   return n1 - n2

# def time(n1, n2):
#   return n1 * n2

# def divide(n1, n2):
#   return n1 / n2

# operations = {
#   "+":add,
#   "-":minus,
#   "*":time,
#   "/":divide,
# }

# def callculator():
#   num1 = float(input("What is the first number? : "))

#   for operation in operations:
#     print(operation)

#   re_calculation = True

#   while re_calculation:
#     operation_symbol = input("pick an operation: ")
#     num2 = float(input("What is the next number? : "))

#     calculation_function = operations[operation_symbol]
#     answer = calculation_function(num1, num2)

#     print(f"{num1} {operation_symbol} {num2} = {answer}")
    
#     if input(f"Type 'y' to continue with {answer}, or type 'n' to exit. : ") == "y":
#       num1 = answer
#     else:
#       re_calculation = False
#       callculator()      

# callculator()


# Quiz_107

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
import random

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card


def calculate_score(cards):
#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
  if sum(cards) == 21 and len(cards) ==2:
    return 0

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
user_cards = []
computer_cards = []
is_game_over = False

for _ in range(2):
  user_cards.append(deal_card())
  computer_cards.append(deal_card())

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

print(f"Your card {user_cards}, score {user_score}")
print(f"computer card {computer_cards[0]}")

if user_score == 0 or computer_score == 0 or user_score > 21:
  is_game_over = True
else:
  user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
  if user_should_deal == "y":
    user_cards.append(deal_card())
  else:
    is_game_over = True

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.




