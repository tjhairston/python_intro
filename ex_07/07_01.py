"""
7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.
You can download the sample data at http://www.py4e.com/code3/words.txt
location: /Users/taylor.hairston/word.txt
"""
print("Assignment 7.1")
#set cd to Users/taylor.hairston/ex_07

file = "words.txt"    # file name: words.txt
try:
    fname=open(file)
except:
    print("Could not open", file)
    quit()


for lx in fname:
    ly = lx.rstrip()
    print(ly.upper())
   
