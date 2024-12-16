# age validator

while True:
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            print("Age cannot be negative!")
        elif age > 120:
            print("That age is unlikely!")
        else:
            print("Your age is:", age)
            break
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")
