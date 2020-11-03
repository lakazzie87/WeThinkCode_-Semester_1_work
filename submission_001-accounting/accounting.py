from user import authentication
from transactions import journal
import banking 
# import banking.fvb.reconciliation as fvb
# import banking.ubsa.reconciliation as ubsa
import sys
import requests
#import user.authentication


for i in range (1, len(sys.argv)):
    print(sys.argv[i])
    
authentication.authenticate_user()
journal.receive_income(100)
journal.pay_expense(100)


banking.fvb.reconciliation.do_reconciliation()
# ubsa.do_reconciliation()

# help("modules")




#packages are files
#modules are .py