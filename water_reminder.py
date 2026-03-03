#Drink water reminder:
#importing notification
from plyer import notification
#importing time
import time
#defining function
def drink_water_reminder():
    notification.notify(
        title = "💧Drink water reminder", 
        message = "Time to drink some water and stay hydrated!",
        timeout = 10
    )

interval = 3600
print("Water reminder started.....")
#running loop
while True:
    drink_water_reminder()

    time.sleep(interval)

