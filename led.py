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