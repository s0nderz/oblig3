def isLeapYear(year):
    if year % 4000 == 0:
        print(str(year) + " is not a leap year")
        return False
    elif year % 4 == 0 and year % 100 != 0:
        print(str(year) + " is a leap year")
        return True
    elif year % 400 == 0:
        print(str(year) + " is a leap year")
        return True
    else:
        print(str(year) + " is not a leap year")
        return False


