import datetime

# Get the current date
current_date = datetime.datetime.now()
print("Current Date:", current_date)

# Subtract 5 days
new_date = current_date - datetime.timedelta(days=5)
print("Date 5 days ago:", new_date)
