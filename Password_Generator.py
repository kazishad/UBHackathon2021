# password generator

import random
import string

#user input for password length
#print(string.ascii_lowercase[1])
user_input = input("How many characters should the password be: ")
#print("User Input: "+ user_input)
special = "!@#$%^&*()[]}{\|,.<>?;:`~"
password_string = ""
#print(special[2])
for i in range(int(user_input)):
    # 1 = number
    # 2 = uppercase letter
    # 3 = lowercase letter
    # 4 = special characters
    character_type = random.randrange(0,5)
    if (character_type == 1):
        password_string+= str(random.randrange(0,9))
    elif (character_type == 2):
        random_character = random.randrange(0,23)
        password_string += string.ascii_uppercase[random_character]
    elif (character_type == 3):
        random_character = random.randrange(0,23)
        password_string += string.ascii_lowercase[random_character]
    elif (character_type == 4):
        random_character = random.randrange(0,23)
        password_string += special[random_character]
print(password_string)


