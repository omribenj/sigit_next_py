def gen_secs():
    """
    generator function to generate seconds in a minute
    """
    for i in range(0, 60):
        yield i

def gen_minutes():
    """
    generator function to generate minutes in an hour
    """
    for i in range(0, 60):
        yield i

def gen_hours():
    """
    generator function to generate hours in a day
    """
    for i in range(0, 24):
        yield i

def gen_time():
    """
    generator function to generate the time in format hh:mm:ss,
    uses the hour, minute and second generators
    """
    hours_gen = gen_hours()
    for hour in hours_gen:
        minutes_gen = gen_minutes()
        for minute in minutes_gen:
            seconds_gen = gen_secs()
            for second in seconds_gen:
                yield "%02d:%02d:%02d" %(hour, minute, second)

def gen_years(start=2019):
    """
    generator function to generate years, starting from the start year
    :param start: the start year, where the count begin
    :type start: int
    """
    year = start
    while 1 == 1:
        yield year
        year += 1

def gen_months():
    """
    generator function to months in a year
    """
    for i in range(1, 13):
        yield i

def gen_days(month, leap_year=True):
    """
    generator function to generate days in a month
    :param month: the number of the month
    :type month: int
    :param leap_year: signifies if the year is a leap year
    :type leap_year: boolean
    """
    number_of_days = 0
    if month in (1,3,5,7,8,10,12):
        number_of_days = 31
    elif month in (4,5,9,11):
        number_of_days = 30
    elif leap_year:
        number_of_days = 29
    else:
        number_of_days = 28
    for i in range(1, number_of_days + 1):
        yield i
    
def gen_date():
    """
    generator function that generates a date
    """
    for year in gen_years():
        is_leap = False
        if (year % 100 == 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
            is_leap = True
        for month in gen_months():
            for day in gen_days(month,is_leap):
                for gt in gen_time():
                    yield "%04d/%02d/%02d" % (day, month, year) + " " + gt

def main():
    # prints the full date every 1000000 iterations.
    date_gen = gen_date()
    count = 0
    # endless loop
    while 1 == 1:     
        if count % 1000000 == 0:
            print(next(date_gen))
        else:
            next(date_gen)
        count += 1
        

if __name__ == "__main__":
    main()

