# date conversions sample
# https://github.com/brunocamps/python-toolkit

# Funcions strftime and strptime


from datetime import datetime
from datetime import *

date = "16/10/2020 00:00:00"

date_time_obj = datetime.strptime(date, '%d/%m/%Y %H:%M:%S')


print ("The type of the date is now",  type(date_time_obj))
print ("The date is", date_time_obj)


# number of months
current_date = datetime.today().strftime('%Y-%m-%d')

print(current_date)
print(type(current_date))

# Function to subtract the difference between two dates and return
# the result in months

def month_diff(d1, d2): 
    diff = (12 * d1.year + d1.month) - (12 * d2.year + d2.month)
    return diff

print(month_diff(datetime.today(), date_time_obj ))