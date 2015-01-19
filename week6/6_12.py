#6_12.py
#Author Siddharth Srinivasan
def sumList(nums):
    a = 0
    for i in nums:
        a = a+i
    return a
 
def main():
    nums = input('Please enter various numbers separate by comma: ')
    nums = nums.split(',')             
    entry = 0
    for i in nums:                 
        nums[entry] = int(i)
        entry = entry+1 
     
    sumTotal = sumList(nums)     
     
    print("Sum of numbers are: ".format(sumTotal))
main()
