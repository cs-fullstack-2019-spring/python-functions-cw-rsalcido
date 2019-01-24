# Problem 1:
#
# Create a function in your program that counts from 0 to [NUMBER]
#
def main():
    problem4()

# def problem1():
#     for numb in range(0,10):
#         print(numb)
# ///////////////////////////////////////////////////////////////////////////////////////////////////

# Problem 2:
#
# We will keep having this problem until EVERYONE gets it right without help
# Create a function that has a loop that quits with ‘q’.
# If the user doesn't enter 'q', ask them to input another string.


# def problem2():
#     userinput = ""
#     while(userinput != 'q' and userinput != 'Q'):
#         userinput = input("please enter another password \n")
#

# /////////////////////////////////////////////////////////////////////////////////////////////////////

# Problem 3:
#
# Create 4 functions called add, subtract, multiply, and divide.
# Create them to allow a user to perform the name of the function to the two numbers and return the result.

# def problem3():
#     num1=int(input("Enter your first number\n"))
#     num2=int(input("Enter your second number\n"))
#
#     print(add(num1,num2),subtract(num1,num2),multiply(num1,num2),divide(num1,num2))
#
# def add(num1,num2):
#     return (num1 + num2)
# def subtract(num1,num2):
#     return (num1 -num2)
# def multiply(num1,num2):
#     return (num1*num2)
# def divide(num1,num2):
#     return (num1/num2)
# ///////////////////////////////////////////////////////////////////////////
# Problem 4:
#
# Create a function that will ask the user for a number.
# Use the function to get two numbers, then pass the two numbers to a function and ask a user if they want to add, subtract, multiple, or divide them.
# Return a string that prints the two numbers, which operation it did, and the result.

def problem4():
    num1=int(input("Enter your first number\n"))
    num2=int(input("Enter your second number\n"))
    num3=(input("Enter what operation we will be performing?"))

    if num3 == 'add':
        print(num1+num2)
    if num3 == 'subtract':
        print(num1-num2)
    if num3 == 'multiply':
        print(num1*num2)
    if num3 == 'divide':
        print(num1/num2)


if __name__ == '__main__':
    main()