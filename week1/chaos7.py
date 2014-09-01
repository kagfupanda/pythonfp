#Author: Siddharth Srinivasan 95016469
#Homework 1 exercise 7

def main():
    x1 = eval(raw_input("Enter a number between 0 and 1 "))
    x2 = eval(raw_input("Enter another number between 0 and 1 "))
    """
    print input in 14 width, left justified
        followed by x1 in width 14, right justified
        followed by blank space in width 14, right justified
        followed by x2 in width 14, right justified
    """
    print("input".ljust(14) + str(x1).rjust(14) + " ".rjust(14) + str(x2).rjust(14))
    #print "-" 60 times
    print("-" * 60)
    for i in range(10):         #loop 10 times
        x1 = 3.9 * x1 * (1 - x1)      # assign to x1
        x2 = 3.9 * x2 * (1 - x2)      # assign to x2
        """
        print blank space in 14 width, left justified
            followed by x1 in width 14, right justified
            followed by blank space in width 14, right justified
            followed by x2 in width 14, right justified
        """
        print(" ".ljust(14) + str(x1).rjust(14) + " ".rjust(14) + str(x2).rjust(14))

       
main()
