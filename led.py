#It makes the light on connection 13 turn on for 1 sec and off for 1 sec.
#Each time it turn on, the terminal will count 1 till 5 as it is in the loop.
from pyfirmata import Arduino, util
import time

board = Arduino('/dev/ttyUSB0')

print ("Incio...")
for i in range(1, 6):
    time.sleep(1)
    print(i)
    board.digital[13].write(1)
    time.sleep(1)
    board.digital[13].write(0)
    time.sleep(1)
print ("FIM...")