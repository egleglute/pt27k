# Find all of the numbers from 1-1000 that are divisible by 6.
# list_of_numbers = [number for number in range (1,1000) if number % 6 == 0]
# print(list_of_numbers)

# Find all number from 1-1000 that have 9 in them.
# list1 = [number for number in range (1,1000) if "9" in str(number)]
# print(list1)

# Given string: text = 'In this lecture we will review some additional functionalities of python built-in data structures.' calculate how many words have letter e in it.
# text = "In this lecture we will review some additional functionalities of python built-in data structures."
# text1 = text.split(" ")
# # print(type(text1))

# how_many = [1 for words in text1 if "e" in words]
# # print(how_many)
# print(sum(how_many))

# Given the same string calculate the occurrence of each letter in the string. (HINT: store everything in dictionary)
# text1 = "In this lecture we will review some additional functionalities of python built-in data structures."
# text2 = list(text1)

# Mano:
# # print(text2)
# squares = {i: text2.count(i) for i in text2 }
# print(squares)

# Eimanto:
# my_dict = {}
 
# for char in text2:
#     if char not in my_dict:
#         my_dict[char] = 1
#     else:
#         my_dict[char] += 1
 
# print(my_dict)

# Mindaugo:
# text = 'In this lecture we will review some additional functionalities of python built-in data structures.'
# my_list = list(text)

# print(f"my_list:\n{my_list}")

# occurences = {letter: text2.count(letter) for letter in text2 if letter != " " and letter != "-" and letter != "."}

# print(occurences)
 
#  Given an object (meet) containing team member names as keys, and their happiness rating out of 10 as the value, you need to assess the overall happiness rating of the group. If <= 5, return 'Get Out Now!'. Else return 'Nice Work Champ!'.
# def vertinimas (name,rating):
while True:
    name = input("Please let us know your name:  ")
    rating = int(input("Please let us know your rating:  "))
    if rating <= 0 or rating >= 10 :
        print("Rating is incorrect value")
    elif rating is >=
        
# print(vertinimas)