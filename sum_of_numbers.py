#!/usr/bin/env python3

# Created By: Val Ijaola
# Date: November 5, 2023
# This program asks the user to enter a positive number.
# It then uses a while loop to add up all the whole numbers,
#  starting from 1, until that number and display the sum to the user.


def main():
    # Input - get user number
    user_number_str = input("Enter an integer. \n")
    try:
        user_number_int = int(user_number_str)
        # declaring variables - sum and counter
        sum = 0
        counter = 0
        while counter < user_number_int:
            counter = counter + 1
            sum = sum + counter
        if user_number_int <= 0:
            print("Enter a positive number")
        else:
            print(f"the total sum is {sum}.")
            print(f"counter = {counter}.")
    except ValueError:
        print(f"{user_number_str} is not an integer.")


if __name__ == "__main__":
    main()
