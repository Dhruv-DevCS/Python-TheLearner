# =========================
# Version 1 — My Original Code
# =========================
# Goal: Generate a random 15-character password
# What I knew at this point:
# - random.randrange
# - loops
# - indexing strings (eg: 'Dhruv' →  0 1 2 3 4 )

import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+=-<>/?,."

i = 1

print("Random Password : ",end='')

for element in chars:

    while(i<=15):
    
        a = random.randrange(0,82)

        print(chars[a],end='')
        i+=1

print("\nDONE!")



print("\n\n")       ##


# =========================
# Version 2 — Improved Version
# =========================
# Improvements:
# 1. Removed unnecessary loop
# 2. Used random.choice instead of index
# 3. Cleaner and more readable
# 4. No Hardcoding (eg: check ln 22)

import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+=-<>/?,."

password = ""

for _ in range(15):

    password += random.choice(chars)

print("Random Password :", password)
print("DONE!")


# '_' as Variable         →  Cleaner & Professional

# random.choice(chars)    →  Picks a Character from 'chars'

# password +=             →  Appends New character infront of Old 'password'
#                         →  same as: password = password + random.choice(chars)
#                                                  xyz12           3         =  xyz123