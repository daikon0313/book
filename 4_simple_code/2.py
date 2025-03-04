###########################
# import os

# key = os.environ.get('TEST_API_KEY')
# print(key)

###########################
# from datetime import date

# today = date.today()
# print(today)
# print(type(today))

###########################
# from datetime import datetime

# now = datetime.now()
# print(now)
# print(type(now))

###########################
from datetime import date
from datetime import datetime

# dt = date(2024, 1, 13)
# tm = datetime(2024, 1, 13, 15, 30, 45)

# tm = datetime(2024, 1, 13, 15, 30, 45)
# y = tm.year
# m = tm.month
# d = tm.day
# h = tm.hour
# mi = tm.minute
# s = tm.second
# micro = tm.microsecond

# print(y, m, d, h, mi, s, micro)

###########################
# d_1 = datetime(2024, 1, 13, 15, 30, 45)
# d_2 = datetime(2024, 1, 13, 17, 30, 45)
# delta = d_2 - d_1
# print(delta)
# print(type(delta))

###########################
from datetime import timedelta
d1 = datetime(2024, 1, 13, 15, 30, 45)
delta = timedelta(days=3, minutes=30)
d2 = d1 + delta
print(d2)