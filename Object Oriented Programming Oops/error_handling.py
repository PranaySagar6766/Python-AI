import sys
import traceback as tb
try :
    dividend = int (input("Enter Dividend :"))
    divisor = int (input ("Enter Divisor"))
    result = dividend/divisor
    print (result)
except ZeroDivisionError as err :
    print (f'{err} : Divisor cannot be zero')
    e_type, e_cause, tb = sys.exc_info()
# prints class and message for an error object
    print (f'{e_type}, {e_cause}')
except ValueError as err:
    print(err)
    tb.print_exc() #prints the traceback
else:
    print("Continue")
finally :
    print ("Always Executes")
