# Nested comprehensions refer to comprehensions where the return value
# is an iteration or other composable logic;
# With nested comps we can do things like build a gameboard; Let's say we wanted a 3x3;
[x for x in range(3)]
# will return [0,1,2];
# but we really want a blank list:
[[] for x in range(3)]
# returns [[],[],[]];
# Now THE BIG PART
# to make the grid we're looking for- we would iterate in our return as well
# remember to return whatever we want our initializing value to be. None works:
[[None for y in range(3)] for x in range(3)];

def gen_square_board(size=3, initial_val = None):
    return [[initial_val for x in range(size)] for y in range(size)]
# read backwords, for each column, we are adding a row with val = None;
# Map + filter comprehensions:
[x*2 for x in range(5) if x%2 == 1]
# consider x % 2 == 1 -> this works as a filter;
# x*2 on the other hand -> works as our map;
# Check out our custom example:
pets = [
    {'name': 'Brian', 'type':'dog', 'sex':'male'},
    {'name': 'Bella', 'type':'dog', 'sex':'female'},
    {'name': 'Henry', 'type':'cat', 'sex':'male'},
    {'name': 'Roxy', 'type':'cat', 'sex':'female'}
]
the_boys = [pet['name'] for pet in pets if pet['sex']=='male'];
dem_dogs = [pet['name'] for pet in pets if pet['type']=='dog'];
# we can also do else statements
# Let's say we have a list of scores in a pass fail system:
scores = [55, 89, 99,87,60,70,74,76,90,82,50];
# We want to convert these to Pass fails;
#This will require a change in syntax:
# [do_this if something else do this for thing in things] <- very useful;
grades = ["Passed!" if score >= 70 else "Failed!" for score in scores]

