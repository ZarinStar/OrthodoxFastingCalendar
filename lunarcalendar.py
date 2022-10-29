#!/usr/bin/python3

from datetime import timedelta, date, datetime

"""
Test:

2019 - March 20, 2019 > April 19 - (Orthodox Easter: April 28)
	April 19 = 9 days later
2020 - April 7 (Orthodox Easter: April 19)
2021 - March 28 (Orthodox Easter: May 2)
2022 - April 16 (Orthodox Easter: April 24)
"""

# Using the paschal full moon and metonic cycle calculations
def paschalFullMoon(year):
	numLunarMonths = 235 #odd is 30, even is 29

	Begindatestring = "2019-03-20" # First full moon: Jan 21 2019 (metonic cycle)
	Begindate = datetime.strptime(Begindatestring, "%Y-%m-%d")
	Enddate = Begindate

	Targetequinoxdatestring = str(year)+"-03-21"
	Targetequinoxdate = datetime.strptime(Targetequinoxdatestring, "%Y-%m-%d")

	while Enddate < Targetequinoxdate: #until we find the first full moon after March 21st of the year
		if (numLunarMonths%2) == 0:
			Enddate = Enddate + timedelta(days=29)
		else:
			Enddate = Enddate + timedelta(days=30)
		numLunarMonths = numLunarMonths - 1

	return Enddate

