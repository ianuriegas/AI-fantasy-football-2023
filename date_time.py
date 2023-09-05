import datetime
import time

def is_start_of_hour(time):
    return time.minute == 52

while True:
    current_time = datetime.datetime.now().time()
    if is_start_of_hour(current_time):
        print("It's the start of the hour!")
    else:
        print("It's not the start of the hour.")
    time.sleep(60)  # Wait for 60 seconds before checking again

current_datetime = datetime.datetime.now()
print(current_datetime.hour, current_datetime.minute, current_datetime)