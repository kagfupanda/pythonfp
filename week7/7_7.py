#7_7.py
#Author Siddharth Srinivasan

def main():
    try:
        timeStart = input("Enter starting time in form HH:MM (01:00-24:59): ")
        timeEnd = input("Enter ending time in form HH:MM (01:00-24:59): ")
        hourStart = int(timeStart[:2])
        minStart = int(timeStart[-2:])
        hourEnd = int(timeEnd[:2])
        minEnd = int(timeEnd[-2:])
        if hourEnd < 21:
            totalbill = ((hourEnd-hourStart)-1)*2.5 + (((60-minStart)+minEnd)/60)*2.5
        elif hourEnd == 21 and minEnd == 0 :
            totalbill = ((hourEnd-hourStart)-1)*2.5 + ((60-minStart)/60)*2.5
        elif hourEnd == 21 and minEnd > 0 :
            before9pm = ((21-hourStart)-1)*2.5 + ((60-minStart)/60)*2.5   
            after9pm = (minEnd/60)*1.75
            totalbill = before9pm+after9pm
        elif hourEnd > 21 :
            before9pm = ((21-hourStart)-1)*2.5 + ((60-minStart)/60)*2.5   
            after9pm = (hourEnd-21)*1.75 + (minEnd/60)*1.75
            totalbill = before9pm + after9pm
        print("Babysitter bill is ${:.2f}".format(totalbill))
         
    except NameError:
        print("Please put in the correct value")
    except:
        print("Something went wrong")
 
main()
