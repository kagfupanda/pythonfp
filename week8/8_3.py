#8_3.py
#Author Siddharth Srinivasan

def doubleYears(start_amt,rate):
    years = 0
    amt = start_amt
    while (amt < 2*start_amt):
        amt = amt + ((float(rate))/100)*amt
        years = years + 1
    remAmt = amt%2
    return years-remAmt

def main():
    initAmt = float(input("Enter initial investment amount: "))
    rate = float(input("Enter the yearly interest rate: "))
    doubleTime = doubleYears(initAmt,rate)
    print("Years to double your investment is: ",doubleTime)

main()
