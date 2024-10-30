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
