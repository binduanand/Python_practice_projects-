import time

def countdown(c):
    while c > 0:
        print(f"{c:02d}", end="\r")
        time.sleep(1)
        c -= 1
    print("Timer Completed!")

c = int(input("Enter the time in seconds: "))
countdown(c)
