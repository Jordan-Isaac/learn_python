""""""

from hello import get_name

print("Welcome to HelloWorld")

first_name, middle_name, last_name = get_name()

user = [first_name, middle_name, last_name]
user_dict = { "first": first_name, "middle": middle_name, "last": last_name, "raw_data": user }

print("Hello", " ".join(user[:]))
