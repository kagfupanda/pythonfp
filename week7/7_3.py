#8_3.py
#Author Siddharth

def main():
    try:
        usrScore = eval(input("Enter your score: "))
        if usrScore > 100:
            print("Too high")
         
        elif usrScore < 0:
            print("Too low")
             
        elif 90 <= usrScore <= 100:
            print("You got an A")
             
        elif 80 <= usrScore < 90:
            print("You got a B")
             
        elif 70 <= usrScore < 80:
            print("You got a C")
         
        elif 60 <= usrScore < 70:
            print("You got a D")
             
        else:   
            print("You got an F")
             
    except NameError:
        print("Correct your number")
    except:
        print("Something went wrong")
         
main()
