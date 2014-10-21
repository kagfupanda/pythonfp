#5_11.py
#chaos program modifyed
#Author Siddharth Srinivasan

def main():
    x1 = eval(input("Enter a number between 0 and 1 "))
    x2 = eval(input("Enter another number between 0 and 1 "))
    x3 = eval(input("Enter how many times you would like to loop: "))
    """
    print input in 14 width, left justified
        followed by x1 in width 14, right justified
        followed by blank space in width 14, right justified
        followed by x2 in width 14, right justified
    """
    print("input".ljust(14) + str(x1).rjust(14) + " ".rjust(14) + str(x2).rjust(14))
    #print "-" 60 times
    print("-" * 60)
    for i in range(x3):         #loop 10 times
        x1 = 3.9 * x1 * (1 - x1)      # assign to x1
        x2 = 3.9 * x2 * (1 - x2)      # assign to x2
        """
        print blank space in 14 width, left justified
            followed by x1 in width 14, right justified
            followed by blank space in width 14, right justified
            followed by x2 in width 14, right justified
        """
        print(str(x3).ljust(14) + str(x1).rjust(14) + " ".rjust(14) + str(x2).rjust(14))

       
main()

