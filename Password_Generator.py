# password generator

import random

#user input for password length
user_input = input("How many characters should the password be:")

for i in range(int(user_input)):
    # 1 = number
    # 2 = uppercase letter
    # 3 = lowercase letter
    # 4 = signs
    character_type = random.randrange(0,9)
    print(character_type)

