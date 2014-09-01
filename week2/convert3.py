#convert3.py
#converts every 10 degress celsius to fahrenhiet
#by Siddharth Srinivasan

def main():
    print("This program lists the calculated conversions every 10 degrees from 0 to 100")
    celsius = 0
    for i in range(11):
        fahrenheit =(celsius * 9/5 ) + 32
        print(celsius, fahrenheit)
        celsius = celsius + 10

main()
