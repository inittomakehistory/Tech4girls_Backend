#integer conversion 
user_input = input("Enter a number: ")

try:
    converted_number = int(user_input)
    print("The number you entered is:", converted_number)
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
