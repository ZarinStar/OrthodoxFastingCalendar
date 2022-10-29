#!/usr/bin/python3

# To run in powershell: py Main.py3
# Note: This uses the 'New calendar' instead of the Old calendar.

import calendar

# MM-DD, days of Fast outside of Wed/Fri
daysOfFast = ['12-24','01-05','08-29','09-14']

def typeOfAbstinence(level):
	if level == 1: #Days of Fast, Christmas Fast (Wed, Fri)
		return "No meat, dairy, fish (except shellfish), olive oil, and wine."
	elif level == 2: #Christmas Fast (Sun, Mon, Tues, Thurs, Sat)
		return "No meat and dairy."
	else:
		return "No fast."

def monthList(date):

	month = int(date[:2])
	year = int(date[3:])
	dayList = []

	rangeTuple = calendar.monthrange(year, month) #returns tuple (weekday, num of days)
	firstWeekday = int(rangeTuple[0])
	numOfDays = int(rangeTuple[1])

	for day in range(1, numOfDays+1):
		weekday = calendar.weekday(year,month,day)
		fastType = determineFast(weekday, day, month, year)
		combinedDate = str(calendar.day_abbr[weekday]) + ' ' + str(month) + '-' + str(day)
		outputString = combinedDate + ": " + fastType	
		dayList.append(outputString)

	return dayList

def determineFast(weekdayInput, dayInput, monthInput, yearInput):

	year = int(yearInput)
	month = int(monthInput)
	day = int(dayInput)
	weekday = int(weekdayInput) # 0 is Mon, 1 is Tues...

	combinedDate = str(month) + '-' + str(day)
	dateType = typeOfAbstinence(0) #default

	if combinedDate in daysOfFast:
		dateType = typeOfAbstinence(1)
	elif weekday == 2 or weekday == 4: #Wed or Fri
		dateType = typeOfAbstinence(1)

	return dateType