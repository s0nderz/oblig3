import random

year_list = []
i = 0
while i < 100:
    year = random.randrange(0, 10000)
    year_list.append(year)
    i += 1

def random_year():
    for i in year_list:
        return i

def isLeapYear():
    if random_year() % 4000 == 0:
        print(str(random_year()) + " is not a leap year")
        return False
    elif random_year() % 4 == 0 and random_year() % 100 != 0:
        print(str(random_year()) + " is a leap year")
        return True
    elif random_year() % 400 == 0:
        print(str(random_year()) + " is a leap year")
        return True
    else:
        print(str(random_year()) + " is not a leap year")
        return False


