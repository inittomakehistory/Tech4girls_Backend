# python basis 
# defining a tuple containing 5 elements 
tuple = (1, "two", 3, "four", 5)

#using indexing to print the first and last elements of the tuple
tuple = (1, "two", 3, "four", 5)
# last elements 
print(tuple[-1]) 

# first element
print(tuple[0]) 


#using of the count() and index() methods on the tuple
# count()
tuple = (1, "two", 3, "four", 5)
new_count = tuple.count("two")
print(new_count)

# index()
tuple = (1, "two", 3, "four", 5)
new_index = tuple. index("four")
print(new_index)


# Converts an integer to a float, a float to an integer, and a string representing a number to an integer
# integer to float 
number = 10
new_number = float(number)
print(new_number)


# float to integer 
number = 7.6
new_number1 = int(number)
print(new_number1)

# string to integer 
number = "6"
new_number2 =int(number)
print(new_number2)

#list of string to a single string 
fruits = [ "apple", "banana", "cherry"]
new=",".join(fruits)
print(new)

