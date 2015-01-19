#7_1.py
#Author Siddharth Srinivasan
def main():
         hours = eval(input("Enter how many hours you worked this week: "))
         rate = eval(input("Enter your hourly rate: "))
         if hours > 40:
                  total = (hours/2) * 7
                  print("You get ", total, "dollars in the week")

         else:
                  total2 = rate * 7
                  print("You get ", total2, "dollars in the week")
main()
