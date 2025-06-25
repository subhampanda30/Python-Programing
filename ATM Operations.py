from ATMExcept import DepositError,WithDrawError,InSuffFundError
bal=500.00 # here bal is called global var
def deposit():
    damt=float(input("Enter Ur Deposit Amount:"))#ValueError
    if(damt<=0):
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print("Ur Account XXXXXXXXXX123 Credited with INR:{}".format(damt))
        print("Ur Account Bal Now:{}".format(bal))

def getWithdraw():
    global bal
    wamt=float(input("Enter the Amount to withdraw:"))
    if(wamt<=0):
        raise WithDrawError
    elif(wamt>bal):
        raise inSuffFundError
    else:
        bal=bal-wamt
        print("Ur Account XXXXXXXXXX123 Credited with INR:{}".format(wamt))
        print("Ur Account Bal Now:{}".format(bal))
def getbalenq():
    print("Ur Account Bal:{}".format(bal))






