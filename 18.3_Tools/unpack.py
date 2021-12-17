#Unpacking works similarly to JS, say we have an iterable like a list:
#NOTE unpackabkle iterables include lists, sets, dicts, tuples, and strs;
names = ['charlie', 'lucy'];
#We can unpack their content by assigning them to vars:
name1, name2 = names;
#works on other iterables too, like tuples:
coord = (100,25);
x,y = coord;

#We can also use the rest operator *:
sorted_scores = [2400,2350,2100,1960];
top_score, *scores = sorted_scores;
#the * operator assigns the remainder of our iterable to the variable its used on
print(scores);
#NOTE unpacking is actually converting and creating a tuple
#behind the scenes we get (x,y) = (coord)
#its actually pretty common to make a tuple withuot parens and not realize it;
#NOTE this matters for complex unpacking, such as when dealing with nested structures;
#in this case we will have to remember we're making tuples and include the ()!

color_pairs = [['red', 'blue'],['orange', 'purple']]
pair1, pair2 = color_pairs;
#if we instead wanted to directly get the vals, not this lists we would do this:
(prim1, sec1), (prim2,sec2) = color_pairs;
#NOTE again py is actually reading: ((...),(...))
#Most common use case: iterating over k,v pairs in a dict:
grade_count = {
    'A': 12,
    'B':20,
    'C':30
}
#We would typically do this:
for pair in grade_count.items():
    print(pair)
#Now we can unpack in line:
for k,val in grade_count.items():
    print(k, val);