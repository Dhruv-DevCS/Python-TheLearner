import random

numerical = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

symbols = ['Hearts', 'Diamond', 'Spades', 'Club']

com_numerical = random.choice(numerical)

com_symbol = random.choice(symbols)

card_com = f"{com_numerical} of {com_symbol}"

while True:
    
    user_numerical = input("Choose from [ 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K' ] : ")
    
    user_symbol = input("Choose from ['Hearts', 'Diamond', 'Spades', 'Club'] : ")

    # Fix 1: correct 'or' syntax
    if user_numerical == 'a' or user_numerical == 'A':
        user_numerical = 1
    
    elif user_numerical == 'j' or user_numerical == 'J':
        user_numerical = 11
    
    elif user_numerical == 'q' or user_numerical == 'Q':
        user_numerical = 12
    
    elif user_numerical == 'k' or user_numerical == 'K':  # Fix 2: was checking 'Q' again
        user_numerical = 13
    
    else:
        user_numerical = int(user_numerical)  # Fix 3: cast to int

    card_user = f"{user_numerical} of {user_symbol}"  # Fix 4: use f-string

    if card_user == card_com:
        
        display_num = {11: 'J', 12: 'Q', 13: 'K', 1: 'A'}.get(com_numerical, com_numerical)
        
        print(f"You Guessed it Right!\nIt was: {display_num} of {com_symbol}")
        
        break

    if user_numerical > com_numerical and user_symbol == com_symbol:
        
        print("Try a Lower Guess")
    
    elif user_numerical < com_numerical and user_symbol == com_symbol:
        
        print("Try a Higher Guess")
    
    elif user_numerical > com_numerical and user_symbol != com_symbol:
        
        print(random.choice(["Try a Lower Guess", "Try Changing the Symbol"]))
    
    elif user_numerical < com_numerical and user_symbol != com_symbol:
        
        print(random.choice(["Try a Higher Guess", "Try Changing the Symbol"]))
    
    elif user_numerical == com_numerical and user_symbol != com_symbol:
        
        print("Try Changing the Symbol")