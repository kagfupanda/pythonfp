#avg2.py
#program to average 3 exam scores
#Illustrates use of multiple input

def main():
    print("This program computes the averge of 3 exam scores.")
    score1, score2, score3 = eval(raw_input("Enter three scores seperated by a comma: "))
    average = (score1 + score2 + score3) / 3
    print("The average of the scores is:", average)


main()
