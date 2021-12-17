#Python has built in functions for reading and writing to files:
#  We can open on-disk files with open(filepath,mode)
    # Mode tells open what to do with a file, r for reading, w for writing, for example;
file = open('helpers.py', 'r');
i = 1
for line in file:
    print(f'Line {i}: {line}');
    i+=1
# Let's say we wanted to also save this to a var -> file text;
file_text = file.read();
# This won't work! 
print(f'''\nfirst time file text is: 
{file_text}''');
# B/c we looped through the file once already, file_text will be set to an empty str;
# To overcome this we will commonly reset our line placement with seek(0);

file.seek(0);
# Now we can access the text again:
file_text = file.read();
print(f'''Second time file text is:

{file_text}''');
file.close();
# Writing to a file
# We do the same thing as before but set the mode to 'w';
file2 = open('write_file.txt', 'w');
# We can write directly to a file:
file2.write('Overridden!')
file2.close();
# This will override the text already in our file.
# Instead we can append by swapping our mode to 'a'
file2 = open('write_file.txt', 'a');
file2.write('\nAppended!')
file2.close();
# We can also create new files by writing to ones that do not exist;
file3 = open('new_file.txt', 'w');
file3.write('Be booorn');