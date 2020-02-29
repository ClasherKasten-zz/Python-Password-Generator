_author_ = "GHaxZ"

import os
import time
import string
import random

clear = lambda:os.system("cls")

print()
print(" ██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░")
time.sleep(0.2)
print(" ██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗")
time.sleep(0.2)
print(" ██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║")
time.sleep(0.2)
print(" ██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║")
time.sleep(0.2)
print(" ██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝")
print(" ╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░")
print()
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
print(" ░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝  ░░░╚═╝░░░╚══════╝")
print()
print()
print()
time.sleep(0.2)
print(" How long should your password be? (min. 8 max. 16)")
print()

loop1 = True
while loop1:
    password_length = input(" ")
    password_length_string = int(password_length)
    if 7 < password_length_string < 17:
        clear()
        print()
        print(" Should it contain special characters?")
        print(" 1 = Yes \n 2 = No")
        print()
        special_characters = input(" ")
        clear()
        break
    else:
        clear()
        print()
        print(" " + password_length + " is not a valid length or not a number.")
        print()
        print(" How long should your password be? (min. 8 max. 16)")
        print()

loop2 = True
while loop2 == True:
    if special_characters == "1":
        if password_length_string == 8:
            def randomStringwithDigitsAndSymbols(stringLength=8):
                password_characters = string.ascii_letters + string.digits + string.punctuation
                return ''.join(random.choice(password_characters) for i in range(stringLength))


            print()
            print(" Your Password:", randomStringwithDigitsAndSymbols())
            print()
            break
        elif password_length_string == 9:
            def randomStringwithDigitsAndSymbols(stringLength=9):
                password_characters = string.ascii_letters + string.digits + string.punctuation
                return ''.join(random.choice(password_characters) for i in range(stringLength))


            print()
            print(" Your Password:", randomStringwithDigitsAndSymbols())
            print()
            break
        elif password_length_string == 10:
            def randomStringwithDigitsAndSymbols(stringLength=10):
                password_characters = string.ascii_letters + string.digits + string.punctuation
                return ''.join(random.choice(password_characters) for i in range(stringLength))


            print()
            print(" Your Password:", randomStringwithDigitsAndSymbols())
            print()
            break
        elif password_length_string == 11:
            def randomStringwithDigitsAndSymbols(stringLength=11):
                password_characters = string.ascii_letters + string.digits + string.punctuation
                return ''.join(random.choice(password_characters) for i in range(stringLength))


            print()
            print(" Your Password:", randomStringwithDigitsAndSymbols())
            print()
            break
        elif password_length_string == 12:
            def randomStringwithDigitsAndSymbols(stringLength=12):
                password_characters = string.ascii_letters + string.digits + string.punctuation
                return ''.join(random.choice(password_characters) for i in range(stringLength))


            print()
            print(" Your Password:", randomStringwithDigitsAndSymbols())
            print()
            break
        elif password_length_string == 13:
            def randomStringwithDigitsAndSymbols(stringLength=13):
                password_characters = string.ascii_letters + string.digits + string.punctuation
                return ''.join(random.choice(password_characters) for i in range(stringLength))


            print()
            print(" Your Password:", randomStringwithDigitsAndSymbols())
            print()
            break
        elif password_length_string == 14:
            def randomStringwithDigitsAndSymbols(stringLength=14):
                password_characters = string.ascii_letters + string.digits + string.punctuation
                return ''.join(random.choice(password_characters) for i in range(stringLength))


            print()
            print(" Your Password:", randomStringwithDigitsAndSymbols())
            print()
            break
        elif password_length_string == 15:
            def randomStringwithDigitsAndSymbols(stringLength=15):
                password_characters = string.ascii_letters + string.digits + string.punctuation
                return ''.join(random.choice(password_characters) for i in range(stringLength))


            print()
            print(" Your Password:", randomStringwithDigitsAndSymbols())
            print()
            break
        elif password_length_string == 16:
            def randomStringwithDigitsAndSymbols(stringLength=16):
                password_characters = string.ascii_letters + string.digits + string.punctuation
                return ''.join(random.choice(password_characters) for i in range(stringLength))


            print()
            print(" Your Password:", randomStringwithDigitsAndSymbols())
            print()
            break

    elif special_characters == "2":
        if password_length_string == 8:
            def randomStringDigits(stringLength=8):
                lettersAndDigits = string.ascii_letters + string.digits
                return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))


            print()
            print(" Your Password:", randomStringDigits())
            print()
            break
        elif password_length_string == 9:
            def randomStringDigits(stringLength=9):
                lettersAndDigits = string.ascii_letters + string.digits
                return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))


            print()
            print(" Your Password:", randomStringDigits())
            print()
            break
        elif password_length_string == 10:
            def randomStringDigits(stringLength=10):
                lettersAndDigits = string.ascii_letters + string.digits
                return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))


            print()
            print(" Your Password:", randomStringDigits())
            print()
            break
        elif password_length_string == 11:
            def randomStringDigits(stringLength=11):
                lettersAndDigits = string.ascii_letters + string.digits
                return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))


            print()
            print(" Your Password:", randomStringDigits())
            print()
            break
        elif password_length_string == 12:
            def randomStringDigits(stringLength=12):
                lettersAndDigits = string.ascii_letters + string.digits
                return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))


            print()
            print(" Your Password:", randomStringDigits())
            print()
            break
        elif password_length_string == 13:
            def randomStringDigits(stringLength=13):
                lettersAndDigits = string.ascii_letters + string.digits
                return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))


            print()
            print(" Your Password:", randomStringDigits())
            print()
            break
        elif password_length_string == 14:
            def randomStringDigits(stringLength=14):
                lettersAndDigits = string.ascii_letters + string.digits
                return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))


            print()
            print(" Your Password:", randomStringDigits())
            print()
            break
        elif password_length_string == 15:
            def randomStringDigits(stringLength=15):
                lettersAndDigits = string.ascii_letters + string.digits
                return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))


            print()
            print(" Your Password:", randomStringDigits())
            print()
            break
        elif password_length_string == 16:
            def randomStringDigits(stringLength=16):
                lettersAndDigits = string.ascii_letters + string.digits
                return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))


            print()
            print(" Your Password:", randomStringDigits())
            print()
            break
    else:
        clear()
        print()
        print(" " + special_characters + " is not a valid answer.")
        print()


print(" You want to write into an external text file?")
print()
print(" 1 = Yes \n 2 = No")
print()

loop3 = True
while loop3 == True:
    write_external_file_ask = input(" ")
    if special_characters == "1":
        if write_external_file_ask == "1":
            clear()
            print()
            print(" What is this password for?")
            print()
            password_for = input(" ")
            my_file = open(password_for + " password.txt", "w+")
            my_file = open(password_for + " password.txt", "r+")
            my_file.write(password_for + " Password: ")
            my_file.write(randomStringwithDigitsAndSymbols())
            my_file = open(password_for + " password.txt", "r")
            clear()
            print()
            print(" Saved in program folder.")
            time.sleep(1.5)
            clear()
            break
        elif write_external_file_ask == "2":
            clear()
            break
        else:
            clear()
            print()
            print(" " + write_external_file_ask + " is not a valid answer.")
            print()
            print(" You want to write into an external text file?")
            print()
            print(" 1 = Yes \n 2 = No")
            print()
    elif special_characters == "2":
        if write_external_file_ask == "1":
            clear()
            print()
            print(" What is this password for?")
            print()
            password_for = input(" ")
            my_file = open(password_for + " password.txt", "w+")
            my_file = open(password_for + " password.txt", "r+")
            my_file.write(password_for + " Password: ")
            my_file.write(randomStringDigits())
            my_file = open(password_for + " password.txt", "r")
            clear()
            print()
            print(" Saved in program folder.")
            time.sleep(1.5)
            clear()
            break
        elif write_external_file_ask == "2":
            clear()
            break
        else:
            clear()
            print()
            print(" " + write_external_file_ask + " is not a valid answer.")
            print()
            print(" You want to write into an external text file?")
            print()
            print(" 1 = Yes \n 2 = No")
            print()



print()
print("  Made by GHaxZ")
print("  GitHub: GHaxZ")
print("  YouTube: GHaxZ")
print("  Discord: GHaxZ#6780")
print()
print(" Thanks for using my password generator!")
time.sleep(3)
exit()
