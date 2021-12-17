#Error handling:
#NOTE Python doesn't throw undefined's like JS instead, its liberal with error messages

# In Js we would get undefined in the following scenarios but not in Py:

# providing too many or too few arguments 
# index beyond the length of list
# using a missing attribute
# retrieving items from dict that doesn't exist
# conversion errors
# dividing by 0;

# In Py we will get errors for these scenarios

# In summation, this means we will need to use try catches far more frequently:
# Let's say we expect a simple dict of name and age:
person = {'name': 'Matt', 'age':25};

def get_age_in_days(person):
    days = person['age'] * 365
    return days;
# This func could get passed a non-dict, a dict without age, or age could be a non-number
# To account for this we would could think up all of these edge cases 
# and create conditionals to account for them, in a look before you leap style approach;
# NOTE the best practice to account for errors is an easier-to-ask-forgiveness style;
# where we wrap our code in a try except loop and see if it works! 
def get_age_in_days(person):
    try:
        days = person['age'] * 365
        return days;
    except:
        print('Error in function get_age_in_days')
# Now we print this err whenever our func errors, but we still haven't handled specific errs:
def get_age_in_days(person):
    try:
        days = person['age'] * 365
        return days;
# We handle specific errors by calling them after except
# We can also save the error as a var to access the cause
    except KeyError as ex_key:
        print(f'Missing key: {ex_key}')
    except TypeError:
        print('Expected person to be a dictionary')
#Error raising:
