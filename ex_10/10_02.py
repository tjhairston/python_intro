"""10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below."""

counts = dict()
fn='mbox-short.txt'
file = open(fn)
for line in file:
    if line.startswith('From '):
        words=line.split()
        time=(words[5])
        hrs=time[0:2]
        counts[hrs] = counts.get(hrs,0)+1

nlist = list()
for k,v in counts.items():
    nlist.append((k,v))
s = sorted(nlist)

for key,val in s:
    print(key,val)