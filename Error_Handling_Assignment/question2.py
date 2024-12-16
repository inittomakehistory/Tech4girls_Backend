#dictionary lookup

data = {"name": "Vicky", "age": 30, "country": "Wonderland"}
try:
key = input("Enter the key you want to look up: ")

    print("Value:", data[key])
except KeyError:
    print(f"Error: Key '{key}' not found in the dictionary.")
