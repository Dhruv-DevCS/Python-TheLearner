# A Function = A Block Of Reusable Code

# Lets take an Example of Printing Happy Birthday 3 Times
#           → No Loops
#           → No Repition of Same Code!
# Therefore,

def happy_birthday():
    print("Happy Birthday to You!")
    print("May U be Eaten By a Snake!")
    print("Happy Birthday to You! HEHEHE")

happy_birthday()

print("\n\n")       # Distinguisher

# We can Even Add Names By using Parameters
# Therefore,

def happy_birthday(name):
    print(f"Happy Birthday to {name}!")
    print("May U be Eaten By a Snake!")
    print(f"Happy Birthday to {name}! HEHEHE")

happy_birthday("Dhruv")

print("")       # Distinguisher

# Or, Add Multiple Names:

happy_birthday("Sam");         
print("")        

happy_birthday("Arthur");       
print("") 

happy_birthday("Karan");        
print("") 

# And If U Tried to Pass more than Given Arguments, 
# It Shoots An Error

# Therefore,

# happy_birthday("Dhruv",16)   
# ERROR!                  ^ More Than Specified Argument

# For it to Run We Need More Parameters

# Therefore, 

def happy_birthday(name,age):
    print(f"Happy Birthday to {name}!")
    print("May U be Eaten By a Snake!")
    print(f"Happy Birthday to {name}! HEHEHE")
    print(f"Grown Ass Aged {age}!")

happy_birthday("Dhruv",17)      # Now That's Great~
print("") 

# But, Thing is Order Matters !
# So,

def happy_birthday(name,age):
    print(f"Happy Birthday to {name}!")
    print("May U be Eaten By a Snake!")
    print(f"Happy Birthday to {name}! HEHEHE")
    print(f"Grown Ass Aged {age}!")

happy_birthday(17,"Dhruv") 
print("WTF!")
print("")

# umm, Yeah! Order Matters ~

