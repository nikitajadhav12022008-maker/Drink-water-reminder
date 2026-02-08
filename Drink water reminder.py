#Drink water reminder:
from plyer import notification
import time

def drink_water_reminder():
    notification.notify(
        title = "💧Drink water reminder", 
        message = "Time to drink some water and stay hydrated!",
        timeout = 10
    )

interval = 3600
print("Water reminder started.....")

while True:
    drink_water_reminder()

    time.sleep(interval)
