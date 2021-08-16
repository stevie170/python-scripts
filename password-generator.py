# password generator: user is prompted for a password length and given a password of that length

import random

# prompt user for password length
pwlength = int(input("Enter the desired password length: ")) 

# create a string that includes all possible characters to use in the password 
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

# generate and display password of desired length by joining the password length with a random sampling of s
p = "".join(random.sample(s,pwlength))
print(p)
