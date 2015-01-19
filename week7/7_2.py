#7_2.py
#Author Siddharth Srinivasan
def main():
         try: 
                  grade = eval(input("Enter your grade on your quiz: "))
         except:
                  print("something went wrong")
         letter = ["A", "B", "C", "D", "F"]
         if grade == 5:
                  print("You got an", letter[0])
         elif grade == 4:
                  print("You got an", letter[1])
         elif grade == 3:
                  print("You got an", letter[2])
         elif grade == 2:
                  print("You got an", letter[3])
         else:
                  print("You got an", letter[4])
main()
