# Simple scipt to find variations of a word.
#Version 1.6
#Thanks to Yiab for the help making this far more efficient.

#import permutations module from itertools library
from itertools import product

#Set string to user input with warning that word has to be lowercase.
s = input("Warning!  Word must be lower case.  Enter word: ")

#looks for all upper and lower case variations
letters = [{ a.upper(), a.lower() } for a in s]
#provides the answer in a list
answer = list(map(''.join,product(*letters)))

print(answer)
