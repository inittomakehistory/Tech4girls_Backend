# python basics 
# a script that defines two boolean variables: is_student and is_employed
# Use and, or, and not to print messages based on the conditions:
# If is_student and is_employed are both True, print "You are a working student."
# If is_student is True but is_employed is False, print "You are a student."
# If not is_student and is_employed, print "You are employed but not a student


is_student = True
is_employed = False
if is_student and is_employed:
  print("You are a working student")
elif is_student:
  print("You are a student")
elif is_employed:
  print("You are employed but not a student")


# a nested if statement that
# asks the user for their age.
# checks if the age is greater than or equal to 18
# If it is, ask if they have a driver's license
# Print "You are allowed to drive." if they do
# If the age is less than 18, print "You are not old enough to drive.

nested if statement 
age = int(input("enter your age:"))
                if age >= 18:
                 license = input ("Do you have a driver's license? (yes/no):")
                      if license.lower() == "yes":
                        print("You are allowed to drive")
                         else:
                           print("You need a driver's license to drive.")
                         else:
                             print("You are not old enough to drive")

