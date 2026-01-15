import time 
import winsound
#set reminder interval in seconds (1 hour = 3600, 2hour = 7200)

interval = 3600 #1hour

while True:
    time.sleep(interval)
    #beep sound
    frequency = 2500 #hz
    duration = 1000 #miliseconds
    winsound.Beep(frequency, duration)
    print("💧time to drink water!!💧")