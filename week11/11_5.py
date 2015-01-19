#11_5.py
#Author Siddharth Srinivasan
def recursive_count(target, nested_num_list):
    count = 0
 
    for element in nested_num_list:
        if type(element) == type([]):
            count += recursive_count(target, element)
        else:
            if element == target:
                count += 1
 
    return count
