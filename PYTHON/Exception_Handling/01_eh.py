try:
    number = int(input("Enter an integer : "))
    print(1 / number)

except ZeroDivisionError:
    print("You can't divide by zero, motherfucker!")

except ValueError:
    print("Please Enter a Valid Number")

# Use below 'Exception' only when all the possible exceptions like ZeroDivisionError and ValueError are already used. Because 'Exception' carries a wide range of exceptions.

except Exception:
    print("Something Went Wrong! pls Try again later!")