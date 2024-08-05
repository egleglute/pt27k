# Create a variables containing strings for username and password. Start endless loop allowing to enter username and password. If credentials are correct stop endless loop and print greeting message.
# username = "labas"
# password = "krabas"

# while True:
#     user_name = input("Enter username :")
#     user_pass = input('Enter password: ')
#     if user_name == username and user_pass == password:
#         print('Welcome')
#         break
#     else:
#         print ('incorrect')
    
# Allow user to enter 10 integers, and then print the sum and average of those entered numbers.
my_list =[]
while True:
    number = int(input("Enter your number: "))
    my_list.append(number)
    if len(my_list) == 10:
        print(f"suma yra : {sum(my_list)}")
        print(f"vidurkis yra : {sum(my_list)/len(my_list)}")
        break
    