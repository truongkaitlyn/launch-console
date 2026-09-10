name = input("What is your name? ")
print(f"Welcome to the Launch Console, {name}!")
console = True
while console:
    print("1. About Me")
    print("2. My Goals")
    print("3. Fun Fact")
    print("4. Exit")
    option = input("Option number? ")
    if option == "1":
        print("Hey, I'm Kaitlyn, and I love crocheting.")
    elif option == "2":
        print("My goals are to learn everyday and create more.")
    elif option == "3":
        print("I play the piano.")
    elif option == "4":
        print("Goodbye.")
        console = False
    else:
        print("Please enter a valid option.")

