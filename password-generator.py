# password generator: user is prompted for a password length and given a password of that length
# This is an application of python and does not necessarily generate secure passwords. A secure password is one that is long and easily remembered, such as a passphrase.
# Passwords such as these (random characters of the desired password length) are more likely to be written down, and thus less secure.
# A good password manager can be a great tool if you want to manage passwords you have a hard time remembering without writing them down.

# if using Python 2, change each instance of input() to raw_input() or you'll get name errors... this was written for Python 3

import random

# prompt user for password length
pwlength = int(input("Enter the desired password length: "))

# if the user entered a password length less than 12, encourage a stronger password length
if pwlength < 16:
    verifylength = input("A strong password length is at least 12 and preferrably 16 or more characters! Do you want a longer password? Y/N ")
    # input validation
    while (verifylength.lower() != 'y' and verifylength.lower() != 'n'):
        verifylength = input("error: wrong input. Please put Y or N only ")
    # respond based on their input
    if verifylength.lower() == 'y':
        pwlength = int(input("Enter the desired password length: "))  # let them enter a longer password length
        while (pwlength < 12):
            pwlength = int(input("error: you wanted a strong password, please enter a length of at least 12! ")) # is it really longer?
    elif verifylength.lower() == 'n':
        print("Sounds good, here is your weak password!")
    else:
        print("I'm not sure what you mean, but here is a not-so-strong a password you could use. Try again if you want a stronger password! \n")
        
# create a string that includes all possible characters to use in the password 
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

# generate and display password of desired length by joining the password length with a random sampling of s
p = "".join(random.sample(s,pwlength))
print(p)
