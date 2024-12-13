import string
import random

s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation

# print(s1)

plen = int(input("Enter your lengt..: "))

s = []
s.extend(s1)
s.extend(s2)
s.extend(s3)
s.extend(s4)

# print(s)
random.shuffle(s)
# print(s)

print("Your password is: ")
print("".join(s[0:plen]))