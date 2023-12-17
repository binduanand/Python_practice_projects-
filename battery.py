import time 
from plyer import notification,battery
charge = battery.status
if(charge["percentage"]==100):
    notification.notify(message=f"LAPTOP IS FULLY CHARGED {charge['percentage']}%", timeout=3)
elif(charge["isCharging"]== True):
    notification.notify(message=f"LAPTOP IS CHARGING \n {charge['percentage']}%", timeout=3)
elif(charge["percentage"]<=20):
     notification.notify(message=f"LOW BATTERY {charge['percentage']}% \n Plugging  in the charger", timeout=3)
