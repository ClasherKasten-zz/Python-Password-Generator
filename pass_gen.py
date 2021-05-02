# Infos
__author__ = "GHaxZ"

# Imports
import os
import time
import string
import random


# Function definitions
clear = lambda:os.system("cls")


def generate_password(password_len=None, special_chars=False):
    if password_len is None:
        raise ValueError("Password length should be defined")
    char_pool = string.ascii_letters + string.digits + (string.punctuation if special_chars else "")
    return "".join((random.choice(char_pool) for i in range(password_len)))


# Intro
print("\n ██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░")
time.sleep(0.2)
print(" ██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗")
time.sleep(0.2)
print(" ██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║")
time.sleep(0.2)
print(" ██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║")
time.sleep(0.2)
print(" ██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝")
print(" ╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░\n")
time.sleep(0.2)
print(" ░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░  ██╗░░░██╗░░███╗░░")
time.sleep(0.2)
print(" ██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗  ██║░░░██║░████║░░")
time.sleep(0.2)
print(" ██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝  ╚██╗░██╔╝██╔██║░░")
time.sleep(0.2)
print(" ██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗  ░╚████╔╝░╚═╝██║░░")
time.sleep(0.2)
print(" ╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║  ░░╚██╔╝░░███████╗")
print(" ░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝  ░░░╚═╝░░░╚══════╝\n\n\n")
time.sleep(0.2)

# Input Password Length and clear screen
while (password_length := int(input(" How long should your password be? (min. 8 max. 16)\n\n "))) < 7 or \
        password_length > 16:
    print(" The password range should be in the range 8 to 16")
clear()

# Input if special characters should be represented in the password and clear screen
special_characters = input("""
 Should it contain special characters?
 1 = Yes
 2 = No
\n """)
clear()

# Generate and output the password
password = generate_password(password_length, special_characters=="1")
print(f" Your generated password: {password}\n")

while (save_password := input(" You want to write into an external text file?\n 1 = Yes \n 2 = No\n\n ")) \
        not in ["1", "2"]:
    print(" This is not a valid answer.")
clear()

if save_password == "1":
    print("\n What is this password for?\n")
    password_usage = input(" ")
    with open(f"{password_usage}_password.txt", "w") as password_vault:
        password_vault.write(f"{password_usage} Password: {password}")
    print("\n Saved in program folder.")
    time.sleep(1.5)
    clear()

# Outro
print("""
 Made by GHaxZ
 GitHub: GHaxZ
 YouTube: GHaxZ
 Discord: GHaxZ#6780")
 
 Thanks for using my password generator!""")
time.sleep(3)
