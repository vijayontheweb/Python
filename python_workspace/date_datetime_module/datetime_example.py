from datetime import datetime

mydatetime = datetime(2021, 10, 3, 14, 20, 1)
print(mydatetime)  # 2021-10-03 14:20:01
mydatetime = mydatetime.replace(year=2020)
print(mydatetime)  # 2020-10-03 14:20:01

datetime1 = datetime(2021, 11, 3, 22, 0)
datetime2 = datetime(2020, 11, 3, 12, 0)  # 1 year and 10 hours apart
# datetime.timedelta(365,36000)	#	i.e. 1 yr=365, 10hrs=36000
datetime1 - datetime2
mydiff = datetime1 - datetime2
mydiff.seconds  # 36000	# Only the seconds including time
mydiff.total_seconds  # 31572000.0	#Everything in seconds including date and time
