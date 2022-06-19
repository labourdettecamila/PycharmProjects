print("Welcome to Disney World")

active = True

while active:
    age = input("Buy a ticket, please enter your age: ")

    if age == "quit":
        active = False

    else:
        try:
            if int(age) < 5:
                print("You're awesome!! Free ticket for you")
            elif int(age) >= 5 and int(age) < 9:
                print("Your ticket costs U$s 15")
            elif int(age) >= 9 and int(age) < 14:
                print("Your ticket costs U$s 23")
            elif int(age) >= 14 and int(age) < 100:
                print("Your ticket costs U$s 35")
            elif int(age) >= 100:
                print("You're awesome!! Free ticket for you")
        except ValueError:
            print ("You can't enter letters. Just numbers greater 0")



