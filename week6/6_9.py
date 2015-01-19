#6_9.py
#Author Siddharth Srinivasan
def grade(score):
         score = eval(input("Enter exam score that you got: "))
         lettergrade = ["A+", "A", "B", "C", "D", "F"]
         if score > 100:
                  return  lettergrade[0] 
         elif score >= 90 and score <= 100:
                  return lettergrade[1]
         elif score >= 80 and score < 90:
                  return lettergrade[2]
         elif score >= 70 and score < 80:
                  return lettergrade[3]
         elif score >= 60 and score < 70:
                  return  lettergrade[4]
         else:
                  return lettergrade[5]
print(grade(""))
         
