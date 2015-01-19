#11_6.py
#Author Siddharth Srinivasan
def flatten(nested_num_list):
    flat_num_list = []
 
    for element in nested_num_list:
        if type(element) == type([]):
            flat_num_list += flatten(element)
        else:
            flat_num_list += [element]
 
    return flat_num_list
