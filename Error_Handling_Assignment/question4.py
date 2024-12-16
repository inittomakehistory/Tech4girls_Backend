# list index access
items = ["apple", "banana", "cherry"]

try:
    index = int(input("Enter the index of the item you want to access: "))
    if index < 0 or index >= len(items):
        raise IndexError
    print("You selected:", items[index])
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
except IndexError:
    print("Error: Index out of bounds. Please enter an index between 0 and", len(items) - 1)
