#volume.py
#This program computes the volume and surface area
#Author Siddharth Srinivasan
import math
def main():
    r = input("Enter a value for your radius of the sphere: ")
    v = (4/3) * math.pi * (r**3)
    a = 4 * math.pi * (r**2)
    print("THe Volume is", v, "and the surface are is", a)

main()
