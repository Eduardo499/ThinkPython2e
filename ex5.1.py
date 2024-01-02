"""
The time module provides a function, also named time, that returns the current Greenwich Mean Time in “the epoch”,
which is an arbitrary time used as a reference point. On UNIX systems, the epoch is 1 January 1970.

{Python}
#>>> import time
#>>> time.time()
1437746094.5735958
Write a script that reads the current time and converts it to a time of day in hours,
minutes, and seconds, plus the number of days since the epoch.
"""

import time


def get_time():
    now = time.time()
    days = int(now // (60 * 60 * 24))
    days_remainder = now % (60 * 60 * 24)
    hours = int(days_remainder // (60 * 60))
    hours_remainder = days_remainder % (60 * 60)
    minutes = int(hours_remainder // 60)
    seconds = hours_remainder % 60
    print(f'{days} days, {hours} hours, {minutes} minutes and {seconds} seconds.')


get_time()
