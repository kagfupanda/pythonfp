#7_6.py
#Author Siddharth Srinivasan
def main():
    trb:
        a = eval(input("Enter the speedlimit"))
        b = eval(input("Enter the clocked speed"))
        if 0 < b  and b <= a:
            print("hour traveled at an acceptable speed limit")
        if b > a and a >=0:
            c = 50 + ((b-a) *5)
            print("hour fine is ${0:0.2f}.".format(c))
        if b>90:
            c = 50+ ((b-a) *5)+200
            print("hour fine is ${0:0.2f}.".format(c))
        if a < 0:
            print("hour can't have a negative speed limit")
        if b < 0:
            print("clock speed can't travel at a negative speed")
        
    except:
            print("Something went wrong")
main()
        
