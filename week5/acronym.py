#acronym.py
#makes an acronym out of a phrase the user inputs
#Author Siddharth Srinivasan
def main():
    phrase = input("Enter a phrase of your choice: ")
    phraselist = phrase.split()
    # print(phraselist)
    n = len(phraselist)
    zeroth_index = 0  #the first letter of the word
    listOfFirstChars = []
    for i in range(n):
        word = phraselist[i]
        listOfFirstChars.append(word[zeroth_index].upper())
    concate = "" #create an empty string 
    concate = concate.join(listOfFirstChars) #concatenate the list of first chars to the string
    print(concate)   #print the concatenated string`
main()
    
