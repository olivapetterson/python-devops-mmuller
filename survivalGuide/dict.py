# Dictionary

pessoa = {
    'name': 'Petterson',
    'age': 28,
}

pessoa.update({'city': 'New York'})  # add a new key-value pair
pessoa['country'] = 'USA'  # add another key-value pair

print(pessoa) # add a new key-value pair
print(type(pessoa)) # Check the type of the object
print(pessoa['name']) # Access the value by key
print(pessoa['city']) # Access the value by key
print(pessoa['country']) # Access the value by key
