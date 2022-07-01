import os
from time import sleep

from dateutil.relativedelta import relativedelta
from datetime import datetime, time, timedelta
import checker

def dateDiffInSeconds(date1, date2):
  timedelta = date2 - date1
  return timedelta.days * 24 * 3600 + timedelta.seconds

def daysHoursMinutesSecondsFromSeconds(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	days, hours = divmod(hours, 24)
	return (days, hours, minutes, seconds)

def clear_terminal():
    sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')


def time_to_pay(now):
  today = now.date()
     
  end_of_month = datetime.strptime(str(today + relativedelta(day=31)) + ' 16:00', '%Y-%m-%d %H:%M')
  if end_of_month.weekday() == 6:
      return end_of_month - timedelta(days=2)
  if end_of_month.weekday() == 5:
      return end_of_month - timedelta(days=1)

  return datetime.strptime(str(end_of_month) + ' 16:00', '%Y-%m-%d %H:%M')

def time_to_vacation():
  vacation_day = input("Please enter your vacation date: (yyyy-mm-dd)\n")

  return checker.check_input(datetime.strptime(vacation_day, '%Y-%m-%d'))

def time_end_workingday():
  today = datetime.today()

  date_time_str = input("In what time you ending? (hh:mm in 24)\n")
        
  return checker.check_input(datetime.strptime(today.strftime("%Y-%m-%d ")  + date_time_str, '%Y-%m-%d %H:%M'))