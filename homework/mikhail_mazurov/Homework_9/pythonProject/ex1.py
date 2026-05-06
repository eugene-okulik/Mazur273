import datetime


people_time = "Jan 15, 2023 - 12:05:33"
python_date = datetime.datetime.strptime(people_time, '%b %d, %Y - %H:%M:%S')
# print(python_date)
print(datetime.datetime.strftime(python_date, '%B'))
print(datetime.datetime.strftime(python_date, '%d.%m.%Y, %H:%M'))
