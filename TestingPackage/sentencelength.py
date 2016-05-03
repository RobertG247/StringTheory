import sys

def main():


    def readfile():
        file=sys.argv[1] #gets the file from the argument
    f=open("textProject.txt","r") #opens the file textProject.txt and reads it
    essay=f.read()
    checkfile(essay)
    f.close()
def checkfile(essay):  # makes a report to check the file
    a=0
    endofsentence=0
    count=len(essay) # counts the length of sentences of the essay
    for a in range(0,count):
        if essay[a]=='.'or essay[a]==','or essay[a]=='!'or essay[a]==';'or essay[a]==':'or essay[a]=='?'or essay[a]=='_'or essay[a]=='-'or essay[a]=='`'or essay[a]=='....'or essay[a]=='""':
            endofsentence+=1 #a for loop with a added list range in it to tell the program where the sentences end.

    words=essay.split()  # a function to "split" the words in the text document
    print(words)

    validwords=0
    testword=0
    b=0
    for a in words:
        testword=words[b]
        testword=len(testword)
        if testword >=3:
           validwords+=1
        b+=1


    numberwords=len(words)
    print("The number of words is",len(words),"The total number of valid words is", validwords)
    print("The average number of words per sentence is",validwords/endofsentence)



main()

# this code still needs improvement to satisfy the 3 character word requirement and to round the final numeric answer to the nearest integer.
    
