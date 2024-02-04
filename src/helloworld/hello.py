"""
This file is the entrypoint for the program.

This module gets the users first, middle, and last name and returns it as a list.

This module leverages utilsjord for the get_name function.

"""

def get_name():
    """
    Takes user input and returns value.
    """
    first = input("what is your first name? : ")
    middle = input("what is your middle name? : ")
    last = input("what is your last name? : ")

    return first, middle, last
