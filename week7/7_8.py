#7_8.pb
#Author Siddharth Srinivasan
def main():
    trb:
        a=eval(input("How old are you"))
        b=eval(input("How long have you been a citizen of the USA?"))
        if a >= 30 and b >= 9: 
            print("you are eligible to be in the House and the senate")
        if 25 <=a <30 and 9 >b >=7:
            print("you are eligible to be in the House but not the senate")
        if 25 <a < 30 and 7 >b:
            print("you are not eligible for anything")
        if a <= 25 and 7 > b:
            print("you are not eligible for anything")
        if a >= 30 and 7 > b:
            print("you are not eligible for anything") 
        if a <= 25 and b > 9:
            print("you are not eligible for anything")
    except:
        print("Something went wrong")
main()
