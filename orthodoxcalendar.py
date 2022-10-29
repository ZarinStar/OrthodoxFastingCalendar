#!/usr/bin/python3

# Note: This uses the 'New calendar' instead of the Old calendar.

import calendar
#import emoji #https://unicode.org/emoji/charts/emoji-list.html
from datetime import timedelta, date, datetime

import lunarcalendar

# MM-DD, days of Fast outside of Wed/Fri
daysOfFast = ['12-24','1-5','8-29','9-14']
theotokoFast = ['8-1','8-2','8-3','8-4','8-5','8-6','8-7','8-8'
				, '8-9','8-10','8-11','8-12','8-13','8-14']

# To determine when is Easter Sunday of a particular year
def easterSunday(yearInput):
	# First Sunday after the first full moon that falls on or after March 21 (Julian calendar)

	#firstFullMoon = lunarcalendar.paschalFullMoon(yearInput)
	if int(yearInput) == 2022:
		return '4-24'
	elif int(yearInput) == 2023:
		return '4-16'
	elif int(yearInput) == 2024:
		return '5-5'

	#return firstFullMoon #test

# To determine when is Pentecost (7th Sunday after Easter)
def pentecostSunday(yearInput):

	date = easterSunday(yearInput)
	easterString = str(date)
	easterDate = datetime.strptime(easterString, "%m-%d")
	pentecostDate = easterDate + timedelta(days=49)
	pentecostDate = str(pentecostDate)

	return pentecostDate

# To determine when is All Saints' Day (Sunday after Pentecost)
def allSaintsSunday(yearInput):
	pentecostString = pentecostSunday(yearInput)
	pentecostDate = datetime.strptime(pentecostString, "%m-%d")
	allSaintsSunday = pentecostDate + timedelta(days=7)
	allSaintsSunday = str(allSaintsSunday)

	return allSaintsSunday

def typeOfAllowedEmoji(level):
	# positive messages instead
	return ""

def typeOfAbstinenceEmoji(level):
	if level == 1: #Days of Fast, Christmas Fast (Wed, Fri), Theotoko's fast (except Sat/Sun)
		#return "No meat, dairy, eggs, fish (except shellfish), olive oil, and wine."		
		return ':cross_mark: :meat_on_bone:,:cheese_wedge:,:egg:,:fish:,:amphora:,:wine_glass:'
	elif level == 2: #Theotoko's fast (Sat/Sun), some Feast Days 
		return ':cross_mark: :meat_on_bone:,:cheese_wedge:,:egg:,:fish:'
	elif level == 3: #Christmas Fast (Sun, Mon, Tues, Thurs, Sat), Holy Apostles
		return ':cross_mark: :meat_on_bone:,:cheese_wedge:,:egg:'
	elif level == 4:
		return ':cross_mark: :meat_on_bone:'
	else:
		return ""

def typeOfAbstinence(level):
	if level == 1: #Days of Fast, Christmas Fast (Wed, Fri), Theotoko's fast (except Sat/Sun)
		return "No meat, dairy, eggs, fish (except shellfish), olive oil, and wine."
	elif level == 2: #Theotoko's fast (Sat/Sun), some Feast Days 
		return "No meat, dairy, eggs, fish (except shellfish)."
	elif level == 3: #Christmas Fast (Sun, Mon, Tues, Thurs, Sat), Holy Apostles
		return "No meat, dairy, and eggs."
	elif level == 4:
		return "No meat."
	else:
		return ""

def monthList(date):

	month = int(date[:2])
	year = int(date[3:])
	dayList = []

	rangeTuple = calendar.monthrange(year, month) #returns tuple (weekday, num of days)
	firstWeekday = int(rangeTuple[0])
	numOfDays = int(rangeTuple[1])

	print(easterSunday(year)) #test

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
	dateType = typeOfAbstinenceEmoji(0) #default

	if combinedDate in daysOfFast:
		dateType = typeOfAbstinenceEmoji(1)
	elif combinedDate in theotokoFast and not(weekday == 2 or weekday == 4):
		dateType = typeOfAbstinenceEmoji(3)
	elif weekday == 2 or weekday == 4: #Wed or Fri
		dateType = typeOfAbstinenceEmoji(1)

	return dateType