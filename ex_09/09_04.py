"""9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer."""

fname = 'mbox-short.txt'
try:
	mbox = open(fname)
except:
	print ('File cannot be opened:', fname)
	exit()

emails = dict()

for line in mbox:
    if line.startswith('From '):
        line = line.split() 
        email=(line[1])
        emails[email]=emails.get(email,0)+1
#print(emails.items())
bigcount = None
bigword = None
for key,value in emails.items():
    if bigcount is None or value>bigcount:
        bigcount = value
        bigword = key
print(bigword,bigcount)
