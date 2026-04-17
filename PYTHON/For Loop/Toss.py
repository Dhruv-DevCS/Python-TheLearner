# =========================
# Version 1 — My Original Code
# =========================
# Goal: Toss a Coin

import random

prob = ['Head','Tails']

def toss():
    input("Press Enter to Toss the Coin>")
    print("You Got", random.choice(prob)+"!\n")

while(True):
    toss()


print("\n")     # Distinguisher


# =========================
# Version 2 — Improved Version
# =========================

import random

probability = ['Head','Tails']

def toss():
    action =  input("Press Enter to Toss the Coin (or 'q' to Exit)>")
    print("You Got",random.choice(probability),"!\n")

    if action == 'q':
        exit()
while True:
    toss()