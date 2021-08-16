# password generator: user is prompted for a password length and given a password of that length
# This is an application of python and does not necessarily generate secure passwords. A secure password is one that is long and easily remembered, such as a passphrase.
# Passwords such as these (random characters of the desired password length) are more likely to be written down, and thus less secure.
# A good password manager can be a great tool if you want to manage passwords you have a hard time remembering without writing them down.

import random

# prompt user for password length
pwlength = int(input("Enter the desired password length: ")) 

# create a string that includes all possible characters to use in the password 
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

# generate and display password of desired length by joining the password length with a random sampling of s
p = "".join(random.sample(s,pwlength))
print(p)
