#8_8.py
#Author Siddharth Srinivasan

def gcd(n, m):
    while m != 0:
        (n, m) = (m, n % m)
    return n

def main():
    try:
        while True:
            v1,v2 = 0,0        
            num1,num2 = eval(input('Enter two different integer numbers separated by a comma: '))
            print("hey..",v1,num1,num2) 
            if int(num1) < 0 or int(num2) < 0:
                v1 = 1
                print('Wrong, please provide only positive integer number!')
            if v1 == 0:
                break
        print('Greatest Common Divisor for {',num1,',',num2,'} is:', gcd(num1,num2))
    except:
        print('Something went wrong!')
    
main()
