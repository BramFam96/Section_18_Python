# Define helpers to use in other file:
from random import randint,choice;
def get_rand_year():
    return randint(1900,2020)
def get_rand_month():
    months = [1,2,3,4,5,6,7,8,9,10,11,12];
    return choice(months)