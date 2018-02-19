import calendar

year = int(input("Enter the birth year: "))
month = int(input("Enter the birth month: "))

print("Here's the calendar you asked for!")
print(calendar.month(year, month))