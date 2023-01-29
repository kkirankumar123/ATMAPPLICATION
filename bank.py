acbal=500
from bankexcept import DepositError
from bankexcept import WithDrawError
from bankexcept import InsuffiFundError
def deposit():
    damt=float(input("Enter amount to deposit:"))
    if (damt<=0):
        raise DepositError
    else:
        global acbal
        acbal=acbal+damt
        print("You have deposited Rs.{} amount".format(damt))
        print("Available balance after deposited: {}".format(acbal))

def withdraw():
    wamt=float(input("Enter amount to withdraw:"))
    if (wamt<=0):
        raise WithDrawError
    else:
        global acbal
        if (wamt>acbal):
            raise InsuffiFundError
        else:
            acbal=acbal-wamt
            print("Take the cash and enjoy")
            print("Available balance after withdraw:{}".format(acbal))

def balenq():
    print("Your Avaialble balance is: {}".format(acbal))
    
    
        
