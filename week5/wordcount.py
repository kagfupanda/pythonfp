#wordcount.py
#program go count number of words
#Author Siddharth Srinivasan
def main():
    phrase = input("Enter a phrase: ")
    words = phrase.split()
    print("The number of words is", len(words))
main()
