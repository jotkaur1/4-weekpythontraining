from datetime import date
print("enter your bday date")
year= int(input("year:"))
month= int(input("month:"))
day= int(input("day;"))
f_date = date(year, month, day)
print(f_date)
print("current date:")
l_date=date.today
print(date.today())
diffrence = l_date - f_date
print(diffrence.days)
