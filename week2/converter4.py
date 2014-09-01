#converter4
#converts from fahrenheit to celsius
#auther Siddharth Srinivasan

def main():
    fahrenheit = input("Enter a number to be converted from fahrenheit to celsius ")
    celsius = (fahrenheit - 32) * 5/9
    print("The temperature is", celsius, "degrees celsius")

main()
