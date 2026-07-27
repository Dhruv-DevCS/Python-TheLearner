# Logic Served by Gemini

# Open main and main1 Side by Side for Better Clarity

import random 

# Start with a completely empty list
scores = [] 

for _ in range(2):
    
    a = -1      # The "Zero Trap" fix
    score = 0
    r = 10

    while True:

        b = random.randrange(r)
        print(b)
        score += 1

        if a == b:
            break

        a = b

    print(f"\nCurrent score : {score}\n")
    
    # INDENTED so it happens every round
    # .append() safely adds the score to the end of the list
    scores.append(score) 

print("\n\nAll Scores:", scores)
print("Average =", sum(scores) / len(scores))