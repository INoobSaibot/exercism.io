def is_leap_year(year):
    if year %4 == 0 and year % 100 != 0:
        result = True
    elif year %4 == 0 and year % 100 == 0 and year % 400 == 0:
        result = True
    else:
        result = False
    return result


def go(a):
    print(is_leap_year(a))
