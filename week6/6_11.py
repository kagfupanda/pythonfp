#6_11.py
#Squares each number in the list
#Author Siddharth Srinivasan
def square(nums):
    n = 0
    for i in nums:
        nums[n] = i**2
        n = n + 1
        
def main():
    nums = input("Enter numbers seperated by commas: ")
    nums = nums.split(',')                                            
    n = 0
    for i in nums:                 
        nums[n] = int(i)
        n = n + 1           
     
    square(nums)              
                                    
    print("Here are the numbers:", nums)
main()

