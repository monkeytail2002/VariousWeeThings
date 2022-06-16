#Built by Angus MacDonald 16/6/22
#Version 1


#Imports os module
import os


#Get directory
dirLocation = input("Please enter file path to search in: ")

#set path variable
path = dirLocation

#confirm path location is correct
pathConfirm = input("Is this the path you want to search in? " + path + " : Y/N?")

if pathConfirm.lower() == 'y':
    #print("yes")
    #Get string being searched for
    userString = input("Enter string to search: ")

    #function for finding text in files.
    def searchString(path):
        os.chdir(path)
        files = os.listdir()
        #print(files)
        for file_name in files:
            #print(file_name)
            abs_path = os.path.abspath(file_name)
            print("Absolute path of the file: ", abs_path)
            #Get the absolute path
            if os.path.isdir(abs_path):
                searchString(abs_path)
            #check all files in path for the matching string
            if os.path.isfile(abs_path):
                with open(file_name, 'r', encoding='latin-1') as f:
                    if userString in f.read():
                        final_path = os.path.abspath(file_name)
                        print(userString + " found in this path " + final_path)
                    else:
                        print("No match found in " + abs_path)

    searchString(path)
elif pathConfirm.lower() == 'n':
    #print("no")
    dirLocation = input("Please enter the right file path to search in: ")
    userString = input("Enter string to search: ")
    def searchString(path):
        os.chdir(path)
        files = os.listdir()
        #print(files)
        for file_name in files:
            #print(file_name)
            abs_path = os.path.abspath(file_name)
            print("Absolute path of the file: ", abs_path)

            if os.path.isdir(abs_path):
                searchString(abs_path)

            if os.path.isfile(abs_path):
                with open(file_name, 'r', encoding='latin-1') as f:
                    if userString in f.read():
                        final_path = os.path.abspath(file_name)
                        print(userString + "found in this path " + final_path)
                    else:
                        print("No match found in " + abs_path)
    #output results
    searchString(path)
else:
    #print("else")
    dirLocation = input("Sorry, it's a yes or no question.  Please try entering the path again:  ")
    userString = input("Enter string to search: ")

    def searchString(path):
        os.chdir(path)
        files = os.listdir()
        #print(files)
        for file_name in files:
            #print(file_name)
            abs_path = os.path.abspath(file_name)
            print("Absolute path of the file: ", abs_path)

            if os.path.isdir(abs_path):
                searchString(abs_path)

            if os.path.isfile(abs_path):
                with open(file_name, 'r', encoding='latin-1') as f:
                    if userString in f.read():
                        final_path = os.path.abspath(file_name)
                        print(userString + " word found in this path " + final_path)
                    else:
                        print("No match found in " + abs_path)

    searchString(path)