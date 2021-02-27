# COMS 3930: Creative Embedded Systems
## Module 2 – Interactive Devices <br> Spencer Bruce 

![Gif of mask with lights being adjusted to show the letters CES lit up on display.](images/CES-mask.gif)

### Included Files

I have uploaded, along with this README, the following files:
- a joystick.ino program to be run on an ESP32 microcontroller. This file is what  sends button, joystick, and switch inputs to the Raspberry Pi.
- a lights.py to be run on the Raspberry Pi on boot, which controls the actions on a 6x10 custom matrix of LED NeoPixel lights in response to the serial input from the ESP32
- an alphabet.py program that stores the dictionary of all the letters in use for one of the mask states

I used a Raspberry Pi Model B with a string of 60 individually-addressable LEDs This string of LEDS was soldered into a matrix and sewn into a face mask given to me by Columbia University. The Python program for controlling the lights in a 2-dimensional fashion was made entirely from scratch and is something I hope to work more on soon!

lights.py was set to run on boot in the `/etc/xdg/lxsession/LXDE-pi/autostart` file. So long as the ESP32 was plugged into the Pi and it was recieving power, the setup is pretty plug-and-play.

A video of me using the PixelMask can be seen [here](https://www.youtube.com/watch?v=pNKkRJZEMz8&feature=youtu.be). 

### Creative Vision
I wanted the PixelMask to be a fun little show of how we've all learned to entertain ourselves going into year 2 of living through a pandemic. To be used either with a friend or with yourself through a mirror, one can draw shapes like a small-scale Lite-Brite, spell out words, or freeze-frame text to be cycled through a rainbow of colors for the world (or nobody else) to see.

### Dependencies
In order to run my program, one needs an ESP32, a Raspberry Pi, and an external
monitor and keyboard for setup. Additionally, I used the following tools to create the project: 
- 60 NeoPixel LEDs
- Some wire + resistors 
- 2 x momentary buttons 
- 1 DPST switch
- 1 analog joystick
- A breadboard
- A very poor quality soldering iron in the mechanical engineering tech lab that nearly burned all of the contacts for solder on my LEDS :( 
- A free Columbia University senior spring COVID-19 apology mask
- A needle and thread
- Patience 

I chose to use [VNC Viewer](www.realvnc.com) for both an external monitor and keyboard. VNC Viewer is a multi-platform remote desktop that allows me to remotely control the Pi from any device. Once the setup is complete, an external montior and keyboard is not needed for casual use of the PixelMask.