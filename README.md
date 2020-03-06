# Pyduino

This is a simple repos with my python codes that I made for run in the arduino. Following is the tutorial steps and issues that I had for set my enviroment.

# How do I set my enviroment for python and arduino.

1) First of all, download the IDE for programming the Arduino on: https://www.arduino.cc/en/main/software
2) Connect your arduino on USB and go to the IDE and follow the path to File > Examples > Firmata > StandardFirmata. Note that it will generate a full code to you. Just click on Upload and it will send this code to your arduino.
  Issue 1 - I've got an error when uploading the code to the arduino "ser_open() can't open device /dev/ttyusb0 permission  denied". To fix it, I runned the command "sudo chmod a+rw /dev/ttyACM0". This happend on Linux, I'm not sure whether it happens in other OS or not. Note that the "ttyACM0" is my arduino on my USB port. It might be different in your computer.
3) Done that, open your favorite Python IDE.
4) The core here is the lib pyfirmata that you import in the code like: "from pyfirmata import Arduino, util".
5) After all, just copy and paste some code on your IDE and run it on the terminal and that's it.
