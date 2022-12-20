import datetime
import time
print("Date and Time\n")

x = 0
while(x<10):
	t = datetime.datetime.now()
	print("Datetime:",t,"\r")
	time.sleep(1)
	x += 1



