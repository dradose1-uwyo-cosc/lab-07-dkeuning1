# Daniel Keunig
# UWYO COSC 1010
# 10/29/2024
# Lab 07
# Lab Section: 11
# Sources, people worked with, help given to: 
## used https://www.w3schools.com/python/ref_string_split.asp to split strings



# Prompt the user for an upper bound 
# Write a while loop that gives the factorial of that upper bound
# This will need to be a positive number
# For this you will need to check to ensure that the user entered a number
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # If a user did not enter a number output a statement saying so
# You will continue to prompt the user until a proper integer value is entered

x = 0
factorial = 1

while x == 0:

    try:
        user_input = int(input("Enter a positive number: "))
        
        if user_input < 0:
            print("Please enter a positive number and try again.")
        
        elif user_input == 0:
            print("The factorial of 0 is 1.")
            x = 1
        
        else:
            while user_input > 0:
                factorial = user_input*factorial
                user_input -= 1

            print(f"The result of the factorial based on the given bound is {factorial}.")
            x = 1

    except(ValueError):
        print("Please enter a positive number and try again.")



    print("*"*75)

# Create a while loop that prompts a user for input of an integer values
# Sum all inputs. When the user enters 'exit' (regardless of casing) end the loop
# Upon ending the loop print the sum
# Your program should accept both positive and negative input
# Remember all inputs from stdin are strings, so you will need to convert the string to an int first
# Before you convert the number you need to check to ensure that it is a numeric string
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # This will return true if every digit in your string is a numerical character
    # However, that means a string such as `-1` would return false, even though your program should accept negative values
    # This means you will need to have a check to see if `-` is first character of the string before you check if it is numerical
    # If it is in the string you will need to remove the `-` character, and know that it will be a negative number, so a subtraction from the overall sum
    # I recommend checking out: https://www.w3schools.com/python/ref_string_replace.asp to figure out how one may remove a character from a string
# All this together means you will have an intensive while loop that includes multiple if statements, likely with some nesting 
# The sum should start at 0 

user_input2 = 0
sum = 0

while user_input2 != 'exit' or 'Exit' or 'EXIT':
    user_input2 = input("Enter a number, type 'exit' to exit. ")
    try:
        user_input2 = int(user_input2)
        sum = sum + user_input2
        print(f"Current Sum: {sum}")
    except(ValueError):
        if user_input2 == 'exit' or 'Exit' or 'EXIT':
            break
        else:
            print("Please enter an integer, or type 'exit' to exit. ")

print(f"Final Sum: {sum}")

print("*"*75)


# Now you will be creating a two operand calculator
# It will support the following operators: +,-,/,*,%
# So accepted input is of the form `operand operator operand`
# You can assume that the user is competent and will only input strings of that form
# You will again need to verify that the operands are numerical values
# For this assume only positive integers will be entered, no need look for negative numbers
# You will need to check the string for which operator it contains
# Once you do, you will need to remove the operands from the string
# This can be done in multiple ways:
    # You can go through the string in a loop and create a substring of the characters until an operator is reached
        # Upon reaching the operator you will switch to another substring and add all characters following to the second new string
    # Alternatively you can use the `.split()` method to split the string around an operator: https://www.w3schools.com/python/ref_string_split.asp
# Your program will need to work with whatever spacing is given
    # So, it should function the same for `5 + 6` as `5+6`
# Print the result of the equation
# Again, loop through prompting the user for input until `exit` in any casing is input

user_equation = ''

while user_equation != "exit":
    user_equation = input("Enter an equation, type 'exit' to exit. ")

    user_equation = user_equation.replace(' ', '')

    print(user_equation)

    if "+" in user_equation:
        equation_list = user_equation.split("+")
        answer = int(equation_list[0]) + int(equation_list[1])

    elif "-" in user_equation:
        equation_list = user_equation.split("-")
        answer = int(equation_list[0]) - int(equation_list[1])

    elif "*" in user_equation:
        equation_list = user_equation.split("*")
        answer = int(equation_list[0]) * int(equation_list[1])

    elif "/" in user_equation:
        equation_list = user_equation.split("/")
        answer = int(equation_list[0]) / int(equation_list[1])

    elif "%" in user_equation:
        equation_list = user_equation.split("%")
        answer = int(equation_list[0]) % int(equation_list[1])

    else:
        equation_list = user_equation
        answer = user_equation

    print(answer)
