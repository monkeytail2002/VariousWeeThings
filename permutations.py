# Simple scipt to find variations of a word.
#Version 1.7
#Thanks to Yiab for the help making this far more efficient.

#import permutations module from itertools library and csv library
from itertools import product
import csv


#Set string to user input with warning that word has to be lowercase.
s = input("Warning!  Word must be lower case.  Enter word: ")

#looks for all upper and lower case variations
letters = [{ a.upper(), a.lower() } for a in s]
#provides the answer in a list
answer = list(map(''.join,product(*letters)))

#set header in csv
header=['Permutations']
#set data in csv
data=[answer]

#open and write to csv
with open('permutations.csv', 'w') as f:
    #set csv writer
    writer = csv.writer(f)
    #write input for csv
    writer.writerow(header)   
    writer.writerow(data)
