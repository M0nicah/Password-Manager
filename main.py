print ("Welcome to Password Manager!")
command = True
while command:                     # commands to guide the user
    print("""
    1.Create New Account
    2.Add a new password
    3.Delete a Password
    4.Generate a new password
    5.Exit/Quit/Log out
    """)
    command = input("What would you like to do? ")
    if command == "1":
        print("Create New Account")
    elif command == "2":
        print("\n Student Deleted")
    elif command == "3":
        print("\n Student Record Found")
    elif command == "4":
        import random
        import string
        LETTERS = string.ascii_letters
        NUMS = "0123456789"
        SPE = '*&^%$+-_!'
        SYMBOLS = LETTERS + NUMS + SPE
        prompt = int(input("Enter password length: "))
        password ="".join(random.sample(SYMBOLS, prompt))
        print("Your new password is " + str(password))

        # print("\n generate")
    elif command == "5":
        print("\n Goodbye!")