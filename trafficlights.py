#Traffic Lights that run 4 times in the terminal.
#Go is the green light that is connected to the connection 13 and will be on for 10 sec.
#Attention is the yellow light that is connected to the connection 11 and will be on for 4 sec.
#Stop is the red light that is connected to the connection 12 and will be on for 8 sec.
from pyfirmata import Arduino, util
import time

board = Arduino('/dev/ttyUSB0')

print ("Begin...")
for i in range(0, 3):
    time.sleep(1)
    print("Go!")
    board.digital[13].write(1)
    time.sleep(10)
    board.digital[13].write(0)
    print("Attention!")
    board.digital[11].write(1)
    time.sleep(4)
    board.digital[11].write(0)
    print("Stop!")
    board.digital[12].write(1)
    time.sleep(8)
    board.digital[12].write(0)
print ("End...")