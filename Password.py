# This program generates a random password based on the user's choice of criteria. 
# The user can choose to generate a password with a specific number of letters, symbols, and numbers

# importing the random module to generate random characters for the password
import random as r
# defining the character sets for letters, numbers, and symbols
string="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
number="0123456789"
symbol="!@#$%^&*()_+-=~`"
# prompting the user to choose the type of password they want to generate
print("Your new password is:")
print("1.Generate a password with 3 letters, 1 symbol and 4 numbers")
print("2.Generate a password with 5 letters, 2 symbols and 3 numbers")
print("3.Generate a password with 7 letters, 3 symbols and 2 numbers")
# getting the user's choice for the type of password to generate
choice = int(input("Enter your choice: "))
# initializing an empty list to store the characters of the generated password
nword=[]
# generating the password based on the user's choice and shuffling the characters to create a random password
if choice == 1:
 for i in range(3):
    nword.append(r.choice(string))
 for i in range(1):
    nword.append(r.choice(symbol))
 for i in range(4):
    nword.append(r.choice(number))
    r.shuffle(nword)
 print("".join(nword))

elif choice == 2:
 for i in range(5):
    nword.append(r.choice(string))      
 for i in range(2):
    nword.append(r.choice(symbol))
 for i in range(3):
    nword.append(r.choice(number))
    r.shuffle(nword)
 print("".join(nword))

elif choice == 3:
 for i in range(7):
    nword.append(r.choice(string))      
 for i in range(3):
    nword.append(r.choice(symbol))
 for i in range(2):
    nword.append(r.choice(number))
    r.shuffle(nword)
 print("".join(nword))
