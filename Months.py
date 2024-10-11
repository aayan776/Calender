import calendar
import datetime
date_time = datetime.datetime.now()
year = date_time.year
year_calender = calendar.calendar(year)
print(year_calender)
month1 = datetime.date(year, 1, 1).strftime("%B")
month2 = datetime.date(year, 2, 1).strftime("%B")
month3 = datetime.date(year, 3, 1).strftime("%B")
month4 = datetime.date(year, 4, 1).strftime("%B")
month5 = datetime.date(year, 5, 1).strftime("%B")
month6 = datetime.date(year, 6, 1).strftime("%B")
month7 = datetime.date(year, 7, 1).strftime("%B")
month8 = datetime.date(year, 8, 1).strftime("%B")
month9 = datetime.date(year, 9, 1).strftime("%B")
month10 = datetime.date(year, 10, 1).strftime("%B")
month11 = datetime.date(year, 11, 1).strftime("%B")
month12 = datetime.date(year, 12, 1).strftime("%B")
print(f"List of months:\n {month1}\n {month2}\n {month3}\n {month4}\n {month5}\n {month6}\n {month7}\n {month8}\n {month9}\n {month10}\n {month11}\n {month12}")