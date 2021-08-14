# accept year then ask the user which calender year he wants the convert
import time
year = int(input("please enter the year "))  # accept year
calender = input("Do you want to convert the year to GC or EC? ")  # do u want to change it to gc or ec
if calender.upper() == "GC":  # if the user types GC convert to gc and print
    converted = year + 8
    print("Gregorian calender " + str(converted))

else:
    converted = year - 8
    print("Ethiopian calender " + str(converted))
time.sleep(30)
