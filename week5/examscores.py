#examscores.py
#Program calculates exam scores to a letter grade
#Author Siddharth Srinivasan
def main():
    numberscore = eval(input("Enter exam score that you got: "))
    lettergrade = ["A+", "A", "B", "C", "D", "F"]
    if numberscore > 100:
        print("Congradulations, you got an", lettergrade[0] + "!")
    elif numberscore >= 90 and numberscore <= 100:
        print("Outstanding job! you got an", lettergrade[1])
    elif numberscore >= 80 and numberscore < 90:
        print("Good job, you got a", lettergrade[2])
    elif numberscore >= 70 and numberscore < 80:
        print("You passed, you got a", lettergrade[3])
    elif numberscore >= 60 and numberscore < 70:
        print("You need to study, you got a", lettergrade[4])
    else:
        print("You failed, you got a", lettergrade[5])
main()
