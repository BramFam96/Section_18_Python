#We can spread iterables into eachother or funcs with the * unpacking operator
fruits = {'apple','banana', 'cherry'}
foods = {'bread', 'noodles', *fruits} 
#NOTE *fruits is the same as [...fruits] in js;
#We can use this to succinctly add iterable data with literal syntax:
test = 'test'
#List:
[*test] == list(test);
#Set:
{*test} == set(test)
#To spread a dictionary we simply use double star
pop_data = {'Nov': 135, 'Dec': 150}
{'Sept': 140, **pop_data};
#we can overide pop_data by passing in new data after the spread
#NOTE we are spreading data void of structure;
nums = [1,2,3,4]
print(nums)
#Abv will print the list including brackets a commas;
print(*nums)
#Will pass nums themselves as individual args;