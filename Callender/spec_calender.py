# ask the user if he want specific month to be displayed and display
import calendar
import time
year = int(input('enter year: '))  # accept input from user
s_m = input("do you want specific month? y/n ")
if s_m.upper() == "Y":
    month = int(input('enter month: '))
    data1 = calendar.month(year, month)
    print(data1)  # print the year and month the user selected
else:
    data = calendar.calendar(year)
    print(data)  # print the entire year's calender
time.sleep(15)
