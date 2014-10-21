#quizgrades.py
#calculates letter grades of quizzes
# Author Siddharth Srinivasan
def main():
    grade = eval(input("Enter your quiz score: "))
    letterGrades = ["F", "F", "D", "C", "B", "A"]
    finalGrade = letterGrades[grade]
    print("Your letter grade is a", finalGrade)
main()
    
        
