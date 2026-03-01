# =========================
# Version 1 — My Original Code
# =========================
# Goal: Generate a random Indian Phone Number.

import random

num = ''
chars = '1234567890'
ini = '789'
i = 0

for _ in range(9):
    
    while(i!=1):
        num += random.choice(ini)
        i+=1;
    
    num+= random.choice(chars)
    
print("Random Phone Number : +91" , num)


print()       # Distiguisher


# =========================
# Version 2 — Improved Version
# =========================
# Improvements:
# Unnecessary While Loop Removal by adding : 'num += random.choice(ini)' before Looping 'for'

import random

num = ''
chars = '1234567890'
ini = '789'

num += random.choice(ini)

for _ in range(9):
    
    num+= random.choice(chars)
    
print("Random Phone Number : +91" , num)


print()       # Distiguisher


# =========================
# Version 3 — More Improved Version
# =========================
# Improvements:
# Very Shortened
# Very Professional and Pythonic
# This is a GENERATOR EXPRESSION !

import random

num = random.choice('789') + ''.join(random.choice('0123456789') for _ in range(9))
print("Random Phone Number : +91", num)

# =========================
# Key Takeaways / Notes
# =========================

# 1. Avoid using while-loops for a single iteration.
# 2. Generator Expressions are useful to make code more Compact.
#     → But They Compromise Readability
# 3. Use '_' as Loop Variable When not Necessary in Further Operations.
#     → But If they are Needed further u may use variables like : i etc...