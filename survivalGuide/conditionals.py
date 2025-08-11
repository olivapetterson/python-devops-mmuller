# Conditionals

a = 99
b = 100

if a > b:
    print(f"{a} is greater than {b}")
elif a == b:
    print(f"{a} is equal to {b}")
else:
    print(f"{a} is less than {b}")

# to control the flow of a program.
# They can also be used in logical operations
# such as and, or, and not.
# Example of logical operations
if a > 50 and b < 150:
    print("Both conditions are true")
if a < 100 or b > 50:
    print("At least one condition is true")
# and can be combined with comparison operators
# such as ==, !=, <, >, <=, and >=.