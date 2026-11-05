# Check Leap Year
year = int(input("enter the year : "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year} year is leap year")
else:
    print(f"{year} year is not leap year")
