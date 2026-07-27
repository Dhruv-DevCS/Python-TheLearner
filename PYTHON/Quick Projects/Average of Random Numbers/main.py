# Original and Flawed

# Open main and main1 Side by Side for Better Clarity

import random 
scores=[0]
z=0
for _ in range(2):
    

    a = -1      # non zero for logic failure below
    score=0
    r = 10

    while True:

        b = random.randrange(r)
        print(b)

        score+=1

        if a==b:
            break

        a = b

    print(f"\nCurrent score : {score}\n")

    scores[z]=score
z+=1


print("\n\n",scores)
print("\n\naverage = ",sum(scores)/len(scores))