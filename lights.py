import board
import neopixel
import time
import serial
import sys
from alphabet import alphabet

angle,joy,blue,green,switch = (0,0,0,0,0)
pixels = neopixel.NeoPixel(board.D21, 60, brightness=0.24, auto_write=True, pixel_order=neopixel.GRB)
ser = serial.Serial('/dev/ttyUSB0', 9600)
time.sleep(1)
ser.readline()
line = str(ser.readline())[2:-3].split("\\t")
angle = line[0]; joy = line[1]; blue = line[2]; green = line[3]; switch = line[4];
mirrored = (switch == "S")
colors = [(255,0,0),(255,165,0),(255,255,0),(0,128,0),(0,0,225),(75,0,130),(238,130,238),(255,255,255),(0,0,0)]
prev_joy = "_"
state = 0
curr = 0
lex =  "abcdefghijklmnopqrstuvwxyz.?! "
stopwatch = 0
i = 0
j = 0

cur_x, cur_y = 0,0
counter = 0
x_, y_ = 5,3
prev = (0,0,0)

def x(xx,y):
    global mirrored
    if not mirrored:
        if y%2 == 0:
            return 10*y - xx + 9
        else:
            return y*10 + xx
    else: 
        if y%2 != 0:
            return 10*y - xx + 9
        else:
            return 10*y + xx

def letter(let, pixels, cur_x = 1, cur_y = 0):
    let = let.upper()
    ret = []
    for i in range(6):
         for ind,pos in enumerate(alphabet[let+str(i)]):
            if pos == "1":
                ret.append((ind,5-i))
    for pos in ret:
       pixels[x(cur_x + pos[0], cur_y + pos[1])] = colors[counter]

    return ret


def mirror(pixels):
    ret = []
    for i in range(6):
        ret += pixels[i*10:(i+1)*10][::-1]
    global mirrored
    mirrored = not mirrored
    return ret


def move(x_, y_, pixels, ang,blu):
    d = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
    global prev
    dire = (0,0)
    if ang  != "_":
        angle = int(ang)
        for i in range(7):
            if angle >= i*45 + 22.5 and angle < ((i+1)*45 + 22.5)%360:
                dire = d[i+1]
                break
        if dire == (0,0) and angle >= 337.5 or angle < 22.5:
            dire = d[0]
    if (x_ + dire[0]<0) or (x_ + dire[0] >= 10):
        dire = (0,dire[1])
    if (y_ + dire[1] < 0) or (y_ + dire[1] >= 6):
        dire = (dire[0],0)

    if blu != "_":
        prev = colors[counter]

    if (x_ + dire[0], y_ + dire[1]) != (x_, y_):
        temp = prev[:]
        prev = pixels[x(x_+dire[0],y_+dire[1])][:]
        pixels[x(x_+dire[0], y_+dire[1])] = colors[counter]
        pixels[x(x_,y_)] = temp
    return x_ + dire[0] , y_ + dire[1]

def clearletter(xxx,y):
    for xx in range(xxx,xxx+3):
        for yy in range(y,6):
            # print(xx,yy, x(xx,yy))
            pixels[x(xx,yy)] = (0,0,0)

while True:
    print(f"\nSTATE: {state}")
    if state ==0:
        pixels[x(x_,y_)] = colors[counter]
    if state == 2:   
        if pixels[x(i,j)] != [0,0,0]:
            pixels[x(i,j)] = colors[counter]
            # time.sleep(0.2)

        if j == 5:  
            i = (i+1)%10
        j = (j+1)%6
        if (i,j) == (0,0):
            counter = (counter +  1)%(len(colors)-1)
       
       
    time.sleep(.05)

    line = str(ser.readline())[2:-3].split("\\t")
    angle = line[0]; joy = line[1]; blue = line[2]; green = line[3]; switch = line[4];
    print(angle, joy, blue, green, switch, mirrored)

    if switch != "S" and mirrored or switch == "S" and not mirrored:
        pixels[:] = mirror(pixels)
        ser.readline()

    if (green != "_"):
        if state == 0 or state  == 2:
            pixels[:] = (0,0,0)*len(pixels)
        if state == 1:
            stopwatch = time.time()
        state = (state + 1)%3
        ser.readline()
        ser.readline()
        ser.readline()
      

    if state == 0:
        x_, y_ = move(x_, y_, pixels, angle, blue)

    elif state == 1:
               
        if (angle == "90"):
            curr =(curr + 1)%len(lex)
            clearletter(cur_x, cur_y)

        elif (angle == "270"):
            curr=(curr-1)%len(lex)
            clearletter(cur_x, cur_y)   
        letter(lex[curr], pixels, cur_x, cur_y)
        if (angle == "180"):
            cur_x = max((0,cur_x - 3));
            clearletter(cur_x, cur_y)
        elif (angle == "0"):
            cur_x = min((9, cur_x + 3))
            clearletter(cur_x, cur_y)
        ser.readline()

    if joy == "Z" and prev_joy == "_" and angle == "_":
        prev_joy = "Z"
        counter = (counter+1)%(len(colors))
        if state == 0:
            pixels[x(x_,y_)] = colors[counter]
        ser.readline()

    elif joy == "_" and prev_joy == "Z":
        prev_joy = "_"
        ser.readline()

    
    
    

