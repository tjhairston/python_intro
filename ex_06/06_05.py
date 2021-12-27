"""6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out."""
print("Exercise 6.5")
text = "X-DSPAM-Confidence:    0.8475";

digit0 = text.find("0")
print(str(digit0))

digit5 = text.find("5")
print(str(digit5))
num = text[digit0:digit5+1]
print(num)




















""""
text = "X-DSPAM-Confidence:    0.8475";
digit0 = text.find('0')
print(digit0)
digit5 = text.find('5')
print(digit5)
number = text[digit0 : digit5+1]
print(number)
numberfloat = float(number)
print(numberfloat)
"""