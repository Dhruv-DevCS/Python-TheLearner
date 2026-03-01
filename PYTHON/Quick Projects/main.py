import math

print("Calculate Logarithm")
print("=" * 40)

# Get the base from user
base_input = input("Enter the base (e, 10, or custom number): ").strip().lower()

if base_input == 'e':
    base = math.e
    base_name = "e"
elif base_input == '10':
    base = 10
    base_name = "10"
else:
    try:
        base = float(base_input)
        base_name = str(base)
    except ValueError:
        print("Invalid base input!")
        exit()

# Get the number to find log of
try:
    number_input = input("Enter the number to find log of: ").strip().lower()
    if number_input == 'e':
        number = math.e
    else:
        number = float(number_input)
except ValueError:
    print("Invalid number input!")
    exit()

# Calculate logarithm
if number <= 0:
    print("Error: Number must be positive!")
else:
    result = math.log(number, base)
    print(f"\nlog_{base_name}({number}) = {result:.6f}")