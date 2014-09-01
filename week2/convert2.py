#convert2.py
#By Siddharth Srinivasan
#Program to convert Celsius to Farenheit

def main():
    print("This program is to convert you input in Celsius to Fahrenheit")
    celsius = eval(raw_input("What is the Celsius temperature? "))
    fahrenheit = (celsius * 9/5) + 32
    for i in range(5):
         print("The temperature is", fahrenheit, "degrees Fahrenheit.")


main()
