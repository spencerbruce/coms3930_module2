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

My mask follows the following three states (as shown in the video above), and you can toggle between them using the green button on the controller:


- LiteBrite mode! You can us the joystick to move the cursor around your mask, pressing the blue button to lay down colors and pressing down on the joystick to change colors.
- Text mode! By using the up/down directions of the joystick to select text and the left/right dirctions to move from one selected character to another, you can write out your own custom text on your mask. By pressing down on the joystick, you can change which color is displayed just as is experienced in the LiteBrite mode.
- Text rainbow mode! Once you have text you enjoy, click the green button to freeze it into place, where the text has a series of color adjustments applied to it pixel-by-pixel. To go back to editing the text or back to LiteBrite mode, you can click the green button again.


I  wanted the PixelMask to be usable alone or with another player. For this reason, the 2-way switch toggles between a mirrored and non-mirrored state. When you're playing alone, you can look in a mirror and control the mask without feeling confused as to which direction to move the joystick. Once you show your creation to  the world, you may simply flip the switch and the outside perspective is as you saw in the mirror.

### Technical Difficulties I Encountered
I was anticipating heading on into the Columbia Makerspace to solder my LED lights together to be sewn into my mask, but unfortunately their soldering station was down. Thankfully I had swipe access to the mech-tech lab where one very poor-quality soldering iron was available to use. I was able to do some of the worst soldering of my life to get the project completed, but it definitely was a close call with many hours of deep breaths. Other than the wiring troubles and ensuring my code ran smoothly, I mostly got to play around with the PixelMask's states!

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