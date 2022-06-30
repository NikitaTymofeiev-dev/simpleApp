from datetime import datetime, time
from dateutil.relativedelta import relativedelta
import sys
from time import sleep

import datefunc
import checker


def choose_date(now):
    datefunc.clear_terminal()
    option = input("Choose counter:\n 1 - time to pay,\n 2 - time to vacation,\n 3 - time to end of working day \n")
    datefunc.clear_terminal()
    if option == '1' or option == 1:

        today = now.date()
        end_of_month = (today + relativedelta(day=31))

        return datetime.strptime(str(end_of_month) + ' 16:00', '%Y-%m-%d %H:%M')
    

    if option == '2' or option == 2:

        vacation_day = input("Please enter your vacation date: (yyyy-mm-dd)\n")

        return checker.check_input(datetime.strptime(vacation_day, '%Y-%m-%d'))
    

    if option == '3' or option == 3:
        
        today = datetime.today()

        date_time_str = input("In what time you ending? (hh:mm in 24)\n")
        
        return checker.check_input(datetime.strptime(today.strftime("%Y-%m-%d ")  + date_time_str, '%Y-%m-%d %H:%M'))
    else:
        print('fuck yourself')
        sys.exit()
    

def main():
    now = datetime.now()
    req = choose_date(now)
    while req>now:
        print("%dd %dh %dm %ds" % datefunc.daysHoursMinutesSecondsFromSeconds(datefunc.dateDiffInSeconds(now, req)))
        datefunc.clear_terminal()
        now = datetime.now()

    print("Thank you")   

if __name__ == "__main__":
    main()
