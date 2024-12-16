# Division Calculator 

while True:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        if denominator == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = numerator / denominator
            print("The result is:", result)
            break
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")
