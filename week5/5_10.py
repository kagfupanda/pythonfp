#5_10.py
#Program calculates average word length in a sentence
#Author Siddharth Srinivasan Period 4
def main():
    sentence = input("Type a sentence: ")
    newSen = sentence.split()

    n = 0
    for i in newSen:
        character = len(i)
        n = n + character
    avrg = (n)/ (len(newSen))
    print(avrg)

main()
        
    
