# This program generates a random password based on the user's choice of criteria. 
# The user can choose to generate a password with a specific number of letters, symbols, and numbers

# importing the random module to generate random characters for the password
import random as r
# defining the character sets for letters, numbers, and symbols
string="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
number="0123456789"
symbol="!@#$%^&*()_+-=~`"
# prompting the user to enter the desired number of letters, symbols, and numbers for the password
x=int(input("Number of Letters :"))
y=int(input("Number of Symbols :"))
z=int(input("Number of Numbers :"))
# initializing an empty list to store the characters of the generated password
nword=[]
# checking if the total length of the password is between 4 and 16 characters, and generating the password accordingly
if 4<=x+y+z<=16:
    for i in range(x):
        nword.append(r.choice(string))
    for i in range(y):
        nword.append(r.choice(symbol))
    for i in range(z):
     nword.append(r.choice(number))
    r.shuffle(nword)
else :
    print("Invalid input. Please enter a total length between 4 and 16 characters.")
  
print("Your new password is:","".join(nword))

