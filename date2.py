import datetime

today=datetime.datetime.now()
yesterday=today-datetime.timedelta(days=1)
tomorrow=today+datetime.timedelta(days=1)

print("Yesterday: ", yesterday.strftime('%Y-%m-%d'))
print("Today: ", today.strftime('%Y-%m-%d'))
print("Tomorrow: ", tomorrow.strftime('%Y-%m-%d'))