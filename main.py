from datetime import datetime, time 
import sys
from time import sleep

import datefunc

def choose_date(now):
    datefunc.clear_terminal()
    option = input("Choose counter:\n 1 - time to pay,\n 2 - time to vacation,\n 3 - time to end of working day \n")
    datefunc.clear_terminal()\

    if option == '1' or option == 1:
        
        return datefunc.time_to_pay(now)
        
    if option == '2' or option == 2:

        return datefunc.time_to_vacation()
    

    if option == '3' or option == 3:
        
       return datefunc.time_end_workingday()
       
    else:
        print('fuck yourself')
        sys.exit()
    

def main():
    now = datetime.now()
    # print(now.today().weekday())
    req = choose_date(now)

    while req>now:
        print("%dd %dh %dm %ds" % datefunc.daysHoursMinutesSecondsFromSeconds(datefunc.dateDiffInSeconds(now, req)))
        datefunc.clear_terminal()
        now = datetime.now()

    print("Thank you")   

if __name__ == "__main__":
    main()
