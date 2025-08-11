# list

name_list = ['Alice', 'Bob', 'Charlie', 21] # list accepts numbers, strings, and other objects

name_list.append('David') # add an element to the end
name_list.extend(['Frank', 'Grace']) # add multiple elements
name_list.insert(1, 'Eve') # insert an element at a specific position
name_list.remove('Charlie') # remove an element by value
print(len(name_list)) # get the length of the list
print("Original list:", name_list)

# ---------------------

# set

name_set = {'Alice', 'Bob', 'Charlie'} # set accepts only unique elements, and does not maintain order

name_set.add('David') # add an element
name_set.update(['Frank', 'Grace']) # add multiple elements
name_set.discard('Charlie') # remove an element by value
print(len(name_set)) # get the number of unique elements in the set
print("Original set:", name_set)

# ---------------------

# tuple

name_tuple = ('Alice', 'Bob', 'Charlie') # tuple is immutable, meaning it cannot be changed after creation

name_tuple = name_tuple + ('David',)  # add an element (tuples are immutable, so this creates a new tuple)
print(len(name_tuple))  # get the length of the tuple
print("Original tuple:", name_tuple)