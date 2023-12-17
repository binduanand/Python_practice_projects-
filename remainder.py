import time 
from plyer import notification
rem = input("What do you want a remainder of?: ")
min = float(input("After how many minutes do you want the remainder?"))
time.sleep(min*60)
notification.notify(title="REMAINDER!!!", message=rem, timeout=10, toast=True)
