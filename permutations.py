# Simple scipt to find variations of a word.
#Version 1.5

#import permutations module from itertools library
from itertools import permutations

#Set string to user input with warning that word has to be lowercase.
s = input("Warning!  Word must be lower case.  Enter word: ")
#Set variable that takes string length from input.
wordl = len(s)

#Set up a list of the user input, and upper and lower case additions of it.
lis2 = list(s)+list(s.upper())+list(s.lower())

#for loop that iterated through the string list by the length of the string.  Prints the permutations.
for x in permutations(lis2, wordl):
    if ''.join(x).lower()==s:
        print(''.join(x))
