from datetime import datetime
from datetime import timedelta


def display_current_datetime():
    current_date = datetime.now()
    current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return current_date
    

def calculate_future_date():
    number_of_day = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.now()
    future_date = current_date + timedelta(days=number_of_day)
    return f"Future date: {str(future_date)[:10]}"

print(display_current_datetime())
print(calculate_future_date())