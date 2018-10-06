import calendar

monthDict = {
    1: ['January', 'january', 'Jan', 'jan', 'JAN', 'JANUARY'],
    2: ['February', 'february', 'Feb', 'feb', 'FEB', 'FEBRUARY'],
    3: ['March', 'march', 'Mar', 'mar', 'MAR', 'MARCH'],
    4: ['April', 'april', 'Apr', 'apr', 'APR', 'APRIL'],
    5: ['May', 'may', 'MAY'],
    6: ['June', 'june', 'JUN', 'JUNE'],
    7: ['July', 'july', 'JUL', 'JULY'],
    8: ['August', 'august', 'Aug', 'AUG', 'AUGUST'],
    9: ['January', 'january', 'Jan', 'jan'],
    10: ['January', 'january', 'Jan', 'jan'],
    11: ['January', 'january', 'Jan', 'jan'],
    12: ['January', 'january', 'Jan', 'jan']

}
year = int(input("Enter the birth year: "))
month = int(input("Enter the birth month: "))

if (month > 12):
    raise IndexError("There's no 13th month!")

if (type(month) == int):
    print("Here's the calendar you asked for!")
    print(calendar.month(year, month))
