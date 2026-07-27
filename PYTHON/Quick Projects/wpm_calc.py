import time
import random

def random_sentence():
    
    string_templates = ["Code is poetry, but debugging is a whole different type of storytelling. Keep your hands on the home row and let the rhythm guide your fingers.",
                    "She realized the map was missing the most important destination. Every adventure begins with a single bold step into the unknown.",
                    "Smooth is fast, and fast is smooth. Let your fingers dance without rushing the rhythm.",
                    "Innovation demands that we embrace the chaos of a blank digital canvas. Every line of software is a building block for a future we cannot yet see.",
                    "Faint whispers echoed through the grand library as old pages turned gently. The scent of aged paper and leather bound books filled the quiet evening air.",
                    "Ink stains covered the mahogany desk while the clock struck twelve times. A brilliant idea finally sparked just as the final candle flickered out."]
    
    return random.choice(string_templates)
    



def wpm_calc():

    print("Welcome to Wpm Calculator!")
    print("Rules :- ")
    print("• You will be given a sentence as a template. You MUST type the sentence correctly for fair test.")
    print("• You will be a given a 3 second countdown before starting the test.")
    print("• Hit Enter After you've done typing so we may match your response with the sentence you are given.")

    while True:

        a = random_sentence()

        print(f"\n\nYour Sentence : \n{a}")
        input("\nHit Enter to Start Coundown>\n")

        for i in range(3, 0, -1):
            print(i)
            time.sleep(1)

        init = time.time()

        text_typed = input("Go! : ")

        if text_typed != a:
            input("Please Type Without Error>")
            continue

        time_taken = (time.time() - init)/60
        print(f"\nTime Taken : {round((time_taken*60),3)} seconds")

        text_len =  len(text_typed)
        print(f"Words      : {round((text_len/5),3)} (approx)")

        wpm = (text_len/5)/time_taken    
        print("WPM        :", round(wpm,0))
        break


if __name__ == "__main__":
    wpm_calc()