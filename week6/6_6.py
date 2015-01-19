#6_6.py
#Program computes area of triangle
#Author Siddharth Srinivasan
import math
def triArea(side1, side2, side3):
         s = (side1 + side2 + side3) / 2
         A = math.sqrt((s-side1) * (s-side2) * (s-side3))
         return A

a = triArea(3, 4, 5)
print(a)
