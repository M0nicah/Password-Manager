
print("Welcome to Password Manager!")
print("Select a command to continue:")
command = True
while command:  # commands to guide the user
    print("""
    1.Create New Account
    2.Sign In
    3.Add a new password
    4.Delete a Password
    5.Generate a new password
    Q.Exit/Quit
    """)
    command = input("What would you like to do? ")
    if command == "1":
        print("Create New Account")
    elif command == "2":
        print("\n Log in")
    elif command == "3":
        print("\n New password saved!")
    elif command == "4":
        print("\n Password deleted successfully")
    elif command == "5":
        import random
        import string

        LETTERS = string.ascii_letters
        NUMS = "0123456789"
        SPE = '*&^%$+-_!'
        SYMBOLS = LETTERS + NUMS + SPE
        prompt = int(input("Enter password length: "))
        password = "".join(random.sample(SYMBOLS, prompt))
        print("\n Password Generated successfully!")
        print("Your new password is " + str(password))
    elif command == "q":
        print("\n Goodbye!")
