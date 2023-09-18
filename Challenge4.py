def is_leap(year):
     if (year % 4 == 0) and (year %100 != 0):
        print(bool(1))
     elif (year % 400) == 0:
        print(bool(1))
     else:
        print(bool(0))

is_leap(2400)
