def fullname(first, middle, last):
    first = first.capitalize()
    middle = middle.capitalize()
    last = last.capitalize()

    return "Name : " + first + " " + middle + " " + last

first = input("Enter First Name : ")
middle = input("Enter Middle Name : ")        
last = input("Enter Last Name : ")            

print(fullname(first,middle,last)) 

print("Done")