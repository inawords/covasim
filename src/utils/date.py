import covasim as cv


def calc_days(start_date):
    """Returns a function that takes a date and returns the days between this date and start_date"""
    def days(date):
        return cv.day(date, start_day=start_date) + 1
    return days
