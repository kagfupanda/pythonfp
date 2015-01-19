#6_13.py
#Author Siddharth Srinivasan
def toNumbers(strList):    
    n = 0
    for i in strList:
        strList[n] = int(i)
        n =  n + 1
     
def main():
    strList = input("Enter values:  ")
    strList = strList.split()
    toNumbers(strList)                     
     
    print(strList)
main()
