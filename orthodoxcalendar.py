#!/usr/bin/python3

# To run in powershell: py Main.py3

import calendar

def typeOfAbstinence(level):
	if level == 1: #Holy Canons, Christmas Fast (Wed, Fri)
		return "No meat, dairy, fish (except shellfish), olive oil, and wine"
	elif level == 2: #Christmas Fast (Sun, Mon, Tues, Thurs, Sat)
		return "No meat and dairy."

def determineDate():

	year = 2022
	month = 10
	day = 28

	#Returns the day of the week (0 is Monday)
	if calendar.weekday(year,month,day) == 2 or calendar.weekday(year,month,day) == 4:
		dateType = typeOfAbstinence(1)

	return dateType