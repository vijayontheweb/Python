import datetime

mytime = datetime.time(2, 20)  # hour, minute, second, microsecond, tzinfo
mytime.minute  # 20
mytime.hour  # 2
print(mytime)  # 02:20:00
mytime.microsecond  # 0

mytime = datetime.time(13, 20, 1, 20)
print(mytime)  # 13:20:01.000020

type(mytime)  # dateime.time

today = datetime.date.today()
print(today)  # Default European	# 2020-06-12
today.year  # 2020
today.month  # 6
today.day  # 12

print(today.ctime())  # 'Fri Jun 12 00:00:00 2020'
