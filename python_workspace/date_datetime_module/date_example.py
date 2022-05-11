from datetime import date
date1 = date(2021, 11, 3)
date2 = date(2020, 11, 3)
result = date1-date2  # datetime.timedelta(365)
print(result)
print(type(result))  # datetime.timedelta
print(result.days)  # 365
