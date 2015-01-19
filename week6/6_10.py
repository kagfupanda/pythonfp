#6_10.py
#Makes an acronmn
#Author Siddharth Srinivasan
def acronym(phrase):
         phrase = input("Enter a phrase: ")
         phraselist = phrase.split()
         n = len(phraselist)
         zeroth_index = 0
         listOfFirstChars = []
         for i in range(n):
                  word = phraselist[i]
                  listOfFirstChars.append(word[zeroth_index].upper())
         concate = ""
         concate = concate.join(listOfFirstChars)
         return concate
print(acronym(""))

      
 

