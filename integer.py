#!/usr/bin/env python3

# Created By: Peter Sobowale
# Date: October 15, 2022
# This program asks the user to enter an integer and
# tells them if it is positive, negative or 0


def main():
    # Get integer user input
    user_integer = int(input("Enter an integer: "))

    # check and display if the integer is positive, negative or 0
    if user_integer > 0:
        print(str(user_integer) + " is a positive number")
    elif user_integer < 0:
        print(str(user_integer) + " is a negative number")
    if user_integer == 0:
        print(str(user_integer) + " is just zero!")


if __name__ == "__main__":
    main()
