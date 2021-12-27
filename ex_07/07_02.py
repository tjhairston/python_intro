""""

7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form: X-DSPAM-Confidence:    0.8475

Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
Desired Output: Average spam confidence: 0.7507185185185187

"""


print("Exercise 7.2")

n = 0 # running count of line
n1 = 0 # for sum


fname = "mbox-short.txt"
try:
    source = open(fname)
    print('File was sucessfully opened')
except:
    print('Could not open file')
    quit()

for line in source:
    if not line.startswith("X-DSPAM-Confidence"): 
        continue
    n = n + 1
    pt1 = line[line.find('0') : ]
    fltpt1 = float(pt1)
    n1 = n1 + fltpt1
avg = n1 / n
print("Average spam confidence:", avg)
