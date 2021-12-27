"""8.5 Open the file mbox-short.txt and read it line by line. 
When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). 
Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'. 
Also look at the last line of the sample output to see how to print the count.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt


fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
"""

from os import read


fname ="mbox-short.txt"
fn = open(fname,"r")
#print(fn.read())

count = 0

for line in fn:
    if line.startswith('From '):
        count = count + 1
        line = line.split()
        print(line[1])
print("There were",count,"lines in the file with From as the first word")