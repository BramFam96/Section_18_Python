# With List comprehension, we are not limited to making lists from lists,
# We can use it to make a list from any iterable data structure;
# These include strings, dictionaries, etc;

# Let's use list comprehension to initialize a dictionary;
daily_count = {day: 0 for day in 'MTWHFSU'}
#We now have our initial dictionary with count set to 0;

#Let's say instead we have an arr of numbers, and we want to make a dict of their squares:

square_dict = {num: num * num for num in range(10)}

#Note, creating a dict with l.comprehension requires the curly braces;
# Sets also require curly braces, but their keys do not have values
# Remember every set filters for repeats:
unique_lets = {let for let in 'alakazam'}
str= 'It was I who lead you to rule those you once feared'
