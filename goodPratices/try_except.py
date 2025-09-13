# Good Practice: Catch specific exceptions
# Bad Practice: Catch all exceptions
try:
    with open("file.txt") as f:
        print(f)
except FileNotFoundError:
    print("File not found")