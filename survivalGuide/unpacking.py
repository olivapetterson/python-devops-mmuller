# unpacking.py

# test = ("Petterson", 28)

# # name = test[0]
# # age = test[1]

# name, age = test


# print(f"Name: {name}, Age: {age}")

people = (
    {"name": "Petterson", "age": 28},
    {"name": "Anna", "age": 22},
    {"name": "John", "age": 30},
    {"name": "Maria", "age": 25}
)

# for person in people:
    # name = person["name"]
    # age = person["age"]
    # print(f"Name: {name}, Age: {age}")
    
# for person in people:
#     name, age = person["name"], person["age"]
#     print(f"Name: {name}, Age: {age}")

# for person in people:
#     name, age = person.values()
#     print(f"Name: {name}, Age: {age}")
    
# for person in people:
#     name, _ = person.values()
#     print(f"Name: {name}")

# first, *middle, last = people

# print (last)

def print_people(name, age):
    print(f"Name: {name} | Age: {age}")
    
for person in people:
    print_people(**person)
    