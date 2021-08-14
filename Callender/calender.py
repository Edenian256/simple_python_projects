import calendar

year = int(input('enter year: '))  # accept input from user
month = int(input('enter year: '))
data1 = calendar.month(year, month)
data = calendar.calendar(year)
print(data1)  # print the year and month the user selected
print(data)  # print the entire year's calender
