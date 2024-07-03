
import datetime
def display_current_datetime():
    current_date = datetime.datetime.now()
    current_date = str(current_date)
    for i,v in enumerate(current_date):
        if v ==".":
            index = i
            break
        
    current_date = f"{current_date[:index]}:{current_date[index+1:index+3]}"
    return f"Current date and time: {current_date}"


def calculate_future_date():
    number_of_day = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.datetime.now()
    future_date = current_date + datetime.timedelta(days=number_of_day)
    return f"Future date: {str(future_date)[:10]}"

print(display_current_datetime())
print(calculate_future_date())