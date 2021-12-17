# In Py our map and filter equivalents are built into succinct function called Comprehensions;
#Say we have the following list:
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13];
# If we want to sort (filter) our even nums into a new list we would do something like:

# evens = [];
# for num in nums:
#     if num % 2 == 0:
#         evens.append(num);

# Now we can complete the same logic in one line with comprehensions
# This a full fledged example:
evens = [num for num in nums if num % 2 == 0];
# with comprehensions we move the result we're looking for from the end of a code block
# to the first arguement in it;

# Let's breakdown this syntax by looking at simpler examples- ones with condtionals:
# If we do not include a conditional, comprehensions work just like map in JS
double = [num*2 for num in nums]
# Note the position of num *2; The equiv code is:
doubled_list = [];
for num in nums:
    doubled_list.append(num*2);

# Square a list;
[num **2 for n in [2,4,6,8]];
# Make list from str;
[char for char in 'test_string'];
# Comprehension on a range generated list 
[(num/2) for num in range(10,20)]
