from forex_python.converter import CurrencyRates, CurrencyCodes
from requests.exceptions import ConnectionError
from sys import *

converter=CurrencyRates()
codes=CurrencyCodes()

def parse_arguments():
    amount=1  #default amount is 1
    try:
        amount=float(argv[1]) # assign vakue to be converted to amount
        del argv[1]
    except ValueError:
        # if no amount is entered use default amount
        pass

    if len(argv) != 4 or argv[2] != 'to':
        raise Exception
    return amount,argv[1].upper,argv[3].upper

usage= '[amount] <BASE> to <DESTINATION>'
try:
    amount, base,dest = parse_arguments()
except:
    print('Usage:')
    print(usage)
    exit(1)





