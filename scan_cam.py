import time
import datetime
from termcolor import colored,cprint
p = 0
while(p<500):
 t = datetime.datetime.now()
 #cprint(t,"\r","green",attrs=['bold'])
 print("Time: ",t,"\r")
 p += 1
 time.sleep(0.4)