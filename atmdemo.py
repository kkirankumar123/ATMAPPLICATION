#atmdemo.py
from atmmenu import atmmenu
from bankexcept import DepositError
from bankexcept import WithDrawError
from bankexcept import InsuffiFundError
from bank import deposit
from bank import withdraw
from bank import balenq

import sys
while(True):
    try:
        atmmenu()
        ch=int(input("Enter your choice:"))
        if(ch==1):
            try:
                deposit()
            except ValueError:
                print("Don't Enter Strs/alphanumeric/special symbols")
            except DepositError:
                print("Don't Enter -VE/ ZERO amount")
        elif(ch==2):
            try:
                withdraw()
            except ValueError:
                print("Don't Enter strs/alphanumeric/specialsymbols")
            except WithDrawError:
                print("Don't enter -VE/ZERO amount")
            except InsuffiFundError:
                print("You don't have sufficent funds to withdraw")
                
        elif(ch==3):
            balenq()
        elif(ch==4):
            print("Thanks for using this app")
            sys.exit()
        else:
            print("Your choice of opeartion is wrong-select properly")
    except ValueError:
        print("Don't enter strs/alphanumeric/special symbols")
        
