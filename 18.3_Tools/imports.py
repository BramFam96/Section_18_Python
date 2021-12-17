# Py contains many useful methods and features that are accessable out of the box;
#It also includes a **standard library** of imports to expand these methods and features;
# NOTE we can find these by searching for the py standard library, and then importing them;
# importing is as simply as writing: 

#  import module;

# Common early-use mod is the random module -> perfect for working with randomized data or nums

# import random;

# NOTE google py random mod, or dir(random);

# We can also import specific methods rather than whole lib;
from random import choice as choose;
from random import *;
#This is also how importing/exporting our own files will work:
# from file import specific_func/*
from helpers import *;
def make_person(name, favColor):
    return {
        'name':name,
        'favColor':favColor,
        'birth_year': get_rand_year(),
        'birth_month': get_rand_month()
    }
# Importing third parties:
# We've already done this with ipython
# we use pip3 install package in our command line and to access our imports globally
