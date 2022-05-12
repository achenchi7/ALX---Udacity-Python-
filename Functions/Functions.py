def readable_timedelta(days):
    week = days//7
    remainder = days%7
    return "{} week(s) and {} day(s)".format(week, remainder)

# test your function
print(readable_timedelta(1000))