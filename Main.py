#!/usr/bin/python3

# To run in powershell: py Main.py3

import orthodoxcalendar

inputString = input("Welcome, what month and year do you want to view? (MM YYYY): ")

calendarList = orthodoxcalendar.monthList(inputString)

for day in calendarList:
	print(day)