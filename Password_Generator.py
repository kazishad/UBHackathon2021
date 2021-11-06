# password generator

import random
import string
def generator():
    #print(string.ascii_lowercase[1])
    #print("User Input: "+ user_input)
    special = "!@#$%^&*()[]}{\|,.<>?;:`~"
    password_string = ""
    #print(special[2])
    for i in range(int(user_input)):
        # 1 = number
        # 2 = uppercase letter
        # 3 = lowercase letter
        # 4 = special characters
        character_type = random.randint(1,4)
        if (character_type == 1):
            password_string+= str(random.randint(0,9))
        elif (character_type == 2):
            random_character = random.randint(0,23)
            password_string += string.ascii_uppercase[random_character]
        elif (character_type == 3):
            random_character = random.randint(0,23)
            password_string += string.ascii_lowercase[random_character]
        elif (character_type == 4):
            random_character = random.randint(0,24)
            password_string += special[random_character]
        
    text_file = open("password.txt", "a")
    text_file.write(password_string)
    text_file.write("\n")
    text_file.close
    print(password_string)

password_multiplayer = input("How many password would you like to generate:")
user_input = input("How many characters should the passwords be: ")
for i in range(int(password_multiplayer)):
    generator()