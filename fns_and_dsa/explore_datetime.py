from datetime import datetime

def display_current_datetime():
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_datetime}")

days = int(input("Enter the number of days to add to the current date: "))
if days < 0:
    print("Please enter a non-negative number of days.")    
else:
    from datetime import timedelta
    from datetime import datetime

def calculate_future_date(days):
    current_datetime = datetime.now()
    future_date = current_datetime + timedelta(days=days)
    formatted_future_date = future_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Future date: {formatted_future_date}")