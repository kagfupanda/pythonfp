#8_2.py
#Author Siddharth Srinivasan
def format():
    print('                            Wind Chill Index')
    print('_____________________________________________________________________________')
    print('    |  -20  |  -10  |   0   |   10  |   20  |   30  |   40  |   50  |   60  |')
    print('_____________________________________________________________________________')
    

def calculations():
         v = 0
         while v <= 50:
                  index = str(v)

                  print(index.center(2),end="  |  ")
                  t = -20
                  while t <= 60:
                           x = 35.74 + 0.6125*t - 35.75*(v**0.16) + 0.4275*t*(v**0.16)
                           x = str(round(x))
                           print(x.center(3),end="  |  ")
                           t = t + 10

                  print()
                  v = v + 5
                  print('_____________________________________________________________________________')
                  
        


         

format()
calculations()
         
