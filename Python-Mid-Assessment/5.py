#Create function to check if date is in given range
from datetime import datetime

def Check_Date(date,start_date,end_date):
    if start_date <= date <= end_date:
        return True
    else:
        return False

date = datetime.strptime("2022-01-01", '%Y-%m-%d')
start_date = datetime.strptime("2021-01-01", '%Y-%m-%d')
end_date = datetime.strptime("2022-12-31", '%Y-%m-%d')
print(Check_Date(date, start_date, end_date))