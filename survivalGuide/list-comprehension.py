# list-comprehension.py

names = ("Petterson", "Findus", "Maja", "Morris") #tuple

# names_list = []
# for name in names:
#     names_list.append(name)

# names_list = [name for name in names if name]  # list comprehension - its the same as the for loop above
# list comprehension is a concise way to create lists

# names_list = [name.upper() for name in names if name] # convert names to uppercase if they are not empty
names_list = [name.upper() for name in names if name.startswith("M")] # filter names starting with "M"

print(names_list)