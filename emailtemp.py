import requests
import bs4
import datetime

current_date = datetime.datetime.now()
print(current_date)
#current_year = current_date.year

#one_day = datetime.timedelta(days=1)
#print(current_date + one_day)

for day_delta in range(1, 6):
    day_add = datetime.timedelta(days=day_delta)
    future_date = current_date + day_add
    print(future_date)

print('hello world')
#print(requests.codes.ok) #equal to 200
#use .raise_for_status() method to check for errors

