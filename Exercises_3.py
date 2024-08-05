# Let user enter name, surname and age. Print if user is allowed to enter an online casino or not. 21 is the age cap.
# Name = input("Please enter your name:  ")
# age = int(input("Please enter your age:  "))
# if age >= 21:
#     print("Welcome")
# else:
#     print("You are not allowed to enter")

# Create a database (list of privileged users), print a specific message with a personal greeting if the user is a privileged and just "Welcome otherwise"
# vartotojai = ["Jonas", "Tomas", "Antanas"]
# privileged_users = ["Petras", "Aluizas"]
# user = input("Please enter your name:  ")
# if user in privileged_users:
#     print(f"Sveiki atvyke, {user}")
# else:
#     print("Welcome otherwise")

# Allow user to enter two numbers, print out which one is higher than the other, or equal.
# Number1 = int(input("Please enter your value:  "))
# Number2 = int(input("Please enter your value:  "))
# if Number1 > Number2:
#     print(f"The following number is higher: {Number1}")
# elif Number2 > Number1:
#     print(f"The following number is higher: {Number2}")
# else:
#     print("Numbers are equal")

# Write a small calculator application, that allows user to enter two numbers and a symbol, do the operation and print the answer.
Number1 = int(input("Please enter your number:  "))    
Number2 = int(input("Please enter your number:  "))
Sign = input("Please enter action wanted (+,-,/,*) :  ")
if Sign == "+":
    x = Number1 + Number2
    
elif Sign == "-":
    x = Number1 - Number2
   
elif Sign == "/":
    x = Number1 / Number2
    
elif Sign == "*":
    x = Number1 * Number2
print(x)    

# Create a number guessing game from 1-10.
# Number = 3
# User_Number = int(input("Please guess the number:  "))
# if User_Number != Number:
#     print("Try again")
# elif User_Number == Number:
#     print("Bingo!")

# Create a variables containing strings for username and password. Start endless loop allowing to enter username and password. If credentials are correct stop endless loop and print greeting message.
# Expected_name = "labas!"
# Expected_pass = "qwerty"
# name = input("Please enter your username:  ")
# password = input("Please enter your password:  ")
# if name == "labas!" and password == "qwerty":
#     print("Welcome")
# else:
#     print("Your credentials are incorrect")

# Allow user to enter 10 integers, and then print the sum and average of those entered numbers.
# my_list = []
# k_1 = int(input("Please enter the number:  "))
# k_2 = int(input("Please enter the number:  "))
# k_3 = int(input("Please enter the number:  "))
# k_4 = int(input("Please enter the number:  "))
# k_5 = int(input("Please enter the number:  "))
# k_6 = int(input("Please enter the number:  "))
# k_7 = int(input("Please enter the number:  "))
# k_8 = int(input("Please enter the number:  "))
# k_9 = int(input("Please enter the number:  "))
# k_10 = int(input("Please enter the number:  "))

# my_listx = k_1 + k_2 + k_3 + k_4 + k_5 + k_6 + k_7 + k_8 + k_9 + k_10
# my_list.append(my_listx)
# for x in my_list:
#     result = 0
#     result += x
#     print(result)
# print(average(my_list))
