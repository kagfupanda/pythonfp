#File: choas.py
# A simple program illustrating chaotic behavior
n = eval(raw_input("How many numbers should I print? "))
def main():
    print("This program illustrates a chaotic function")
    x = eval(raw_input("Enter a number between 0 and 1: "))
    for i in range(n):
        x = 2.0 * x * (1-x)
        print(x)

main()



