import datetime

date = datetime.datetime.now()
year_now = date.year
print(year_now)
birth_year = int(input("Enter your birth year: "))
age = year_now - birth_year

print("Your Age is: " + str(age))


weight_in_pounds = float(input("Enter your weight in LBS: "))
weight_in_kilograms = weight_in_pounds * 0.45359237
print(f"Your weight in Kilograms is: {str(weight_in_kilograms)}")   # Just another way of representing the strings
