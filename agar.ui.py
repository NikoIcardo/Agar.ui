from tkinter import *
import keyboard
import time
import random 


BoardSizeX = 1920
BoardSizeY = 1080

################################################################################################################

#Variables

#MainScreen
MainScreen = Canvas(master, width = BoardSizeX, height = BoardSizeY)
MainScreen.pack()

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)

MainScreen.create_circle =  _create_circle

master.wm_title("Agar.iu")

bit = bits()


#bits
bitList = list()
for i in range(300):
    bit = bits()
    bitList.append(bit)

#enemy
enemyList = list()
for i in range(300):
    enemy = enemies()
    enemyList.append(enemy)

    

#character vars
x = 100;
y = 100;
r = 10;

# Game State
Alive = True





################################################################################################################
#Classes

class bits:
    def __init__(self):

        #color
        de=("%02x"%random.randint(0,255))
        re=("%02x"%random.randint(0,255))
        we=("%02x"%random.randint(0,255))
        ge="#"
        color=ge+de+re+we
        #
        
        self.x = random.randint(0, BoardSizeX)
        self.y = random.randint(0, BoardSizeY)
        self.color = color



class enemies:
    def __init__(self):

        #color
        de=("%02x"%random.randint(0,255))
        re=("%02x"%random.randint(0,255))
        we=("%02x"%random.randint(0,255))
        ge="#"
        color=ge+de+re+we
        #
        
        self.x = random.randint(0, BoardSizeX)
        self.y = random.randint(0, BoardSizeY)
        self.color = color
        self.r = 10



        

################################################################################################################

#Functions
        
def UpdateScreen():
    #Screen
    MainScreen.delete("all")

    #Draw Character
    MainScreen.create_circle(MainScreen, x, y, r, fill = "#fb0", outline = "#DDD", width = 1)

    #Draw Bits
    for i in range(0, len(bitList)):
        bit = bitList[i]
        
        MainScreen.create_circle(MainScreen, bit.x, bit.y, 4, fill = bit.color, outline = "#DDD", width = 1)
        
    #Draw Enemies
    for i in range(0, len(bitList)):
        bit = bitList[i]
        
        MainScreen.create_circle(MainScreen, bit.x, bit.y, 4, fill = bit.color, outline = "#DDD", width = 1)
    
    MainScreen.update()
    
    time.sleep(.01)


################################################################################################################


#Main Loop
while Alive:

    #eat bit
    for i in range(0, len(bitList)):
        if bitList[i].x <= x + r and bitList[i].x >= x - r:
            if bitList[i].y <= y + r and bitList[i].y >= y - r:
                bitList[i] = bits()
                r += .07
  
    #movement

    if keyboard.is_pressed('a'):
        x -= 100/r;
        print("hello")
    if keyboard.is_pressed('d'):
        x += 100/r;
        print("d")
    if keyboard.is_pressed('s'):
        y += 100/r;
        print("s")
    if keyboard.is_pressed('w'):
        y -= 100/r;
        print("w")

    UpdateScreen()
