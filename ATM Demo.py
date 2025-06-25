from ATMMenu import menu
import sys
from ATMOperations import deposit,getwithdraw,getbalenq
from ATMExcept import DepositError,WithDrawError,InSuffFundError
while(True):
    try:
        menu()
        ch=int(input("Enter Ur Choice:"))
        match(ch):
            case 1:
                try:
                    deposit()
                except DepositError:
                    print("Don't Deposit Zero for-Ve amount")
                except ValueError:
                    print("Don't try to deposit alnums,str and symbols")
            case 2:
                try:
                    getwithdraw()
                except WithDrawError:
                    print("Don't withdraw zero for -ve amount")
                except InsuffFundError:
                    print("Ur Account does not have funds--Read Python Notes")
                except ValueError:
                    print("Don't try to withdraw alnums,strs and symbols")
            case 3:
                    getbalenq()
            case 4:
                    print("Thx for using this program")
                    sys.exit()
            case _:
                    print("Ur Selection of Operation is wrong--try agian")
    except ValueError:
        print("Don't enter alnums,strs and symbols for choice:")



















