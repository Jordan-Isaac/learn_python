from hello import get_name

print("Welcome to HelloWorld")

# Get the user's names using the get_name function
first_name, middle_name, last_name = get_name()

# Create a list and dictionary to store user data
user = [first_name, middle_name, last_name]
user_dict = {"first": first_name, "middle": middle_name, "last": last_name, "raw_data": user}

# Print a personalized greeting
print("Hello", " ".join(user[:]))

#try again

# main.py
from hello import get_name

print("Welcome to HelloWorld")

first_name, middle_name, last_name = get_name()

user = [first_name, middle_name, last_name]
user_dict = {"first": first_name, "middle": middle_name, "last": last_name, "raw_data": user}

print("Hello", " ".join(user[:]))
