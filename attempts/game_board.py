def start_game():
    print("X - O GAME")
    print("")
    while True:
        print("Choose what action you would like to take:")
        print("1.Start game")
        print("2.Exit")
        action_taken = int(input("Please write 1 or 2 action you want to take:  "))
        if action_taken == 1:
            print("Welcome")  
            break
        else:
            print("Bye!")
