"""
8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
You can download the sample data at http://www.py4e.com/code3/romeo.txt
"""
#read file, create empdty list []
wordlist = []
fname='romeo.txt'  #input("Enter file name: ")
list=open(fname)
print(list)
for word in list:
    words = word.split()
    for word in words:
        if word in wordlist: 
            continue
        wordlist.append(word)
swordlist = sorted(wordlist)
print(swordlist)
print(len(swordlist))