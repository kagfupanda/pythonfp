#11_7.py
#Author Siddharth Srinivasan
def readposint(prompt = 'Please enter a positive integer: '):
    while True:
        posint = raw_input(prompt)
        try:
            posint = float(posint)
            if posint != int(posint):
                raise ValueError, '%s is not an integer' % posint
            elif posint < 1:
                raise ValueError, '%s is not positive' % posint
            break
        except:
            print '%s is not a positive integer. Try again.' % posint
 
    return int(posint)
