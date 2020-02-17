from tkinter import *
import keyboard
import time
import random
import math
#fuck you

BoardSizeX = 1920
BoardSizeY = 1080


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
        ###

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
        ###

        self.x = random.randint(0, BoardSizeX)
        self.y = random.randint(0, BoardSizeY)
        self.color = color
        self.r = 10
        self.movement = 100/self.r + self.r*.01





################################################################################################################



#Variables

master = Tk()

#MainScreen
MainScreen = Canvas(master, width = BoardSizeX, height = BoardSizeY)
MainScreen.pack()

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)

MainScreen.create_circle =  _create_circle

master.wm_title("Agar.iu")



#bits
bitList = list()
for i in range(500):
    bit = bits()
    bitList.append(bit)

#enemy
enemyList = list()
for i in range(10):
    enemy = enemies()
    enemyList.append(enemy)



#character vars
x = 100
y = 100
r = 10
area = 3.14 * r ** 2

# Game State
Alive = True

#Movement
movementSpeed = 100/r + r*.01


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
    for i in range(0, len(enemyList)):
        enemy = enemyList[i]

        MainScreen.create_circle(MainScreen, enemy.x, enemy.y, enemy.r, fill = enemy.color, outline = "#DDD", width = 1)

    MainScreen.update()

    time.sleep(.0001)




################################################################################################################


#Main Loop
while Alive:

    #eat bit
    for i in range(0, len(bitList)):
        if bitList[i].x <= x + r and bitList[i].x >= x - r:
            if bitList[i].y <= y + r and bitList[i].y >= y - r:
                bitList[i] = bits()
                r += .07
                area = 3.14 * r ** 2


    #Update Enemy

    for i in range(0, len(enemyList)):
        if enemyList[i].x <= x + r and enemyList[i].x >= x - r:
            if enemyList[i].y <= y + r and enemyList[i].y >= y - r:
                area += 3.14 * enemyList[i].r ** 2
                r = math.sqrt(area/(3.14))
                enemyList[i] = enemies()
>>>>>>> 968e97c93ac48e9e97d0d13a947e6b2f160e5ccf

        enemyList[i].x += ((-1)**random.randint(0,1))*enemyList[i].movement
        enemyList[i].y += ((-1)**random.randint(0,1))*enemyList[i].movement

        #enemy eats bits
        for j in range(0, len(bitList)):
            e = enemyList[i]
            if bitList[j].x <= e.x + e.r and bitList[j].x >= e.x - e.r:
                if bitList[j].y <= e.y + e.r and bitList[j].y >= e.y - e.r:
                    bitList[j] = bits()
                    e.r += 1

    #movement



    if keyboard.is_pressed('a'):
<<<<<<< HEAD
        x -= movementSpeed 
        
    if keyboard.is_pressed('d'):
        x += movementSpeed 
        
    if keyboard.is_pressed('s'):
        y += movementSpeed 
        
    if keyboard.is_pressed('w'):
        y -= movementSpeed 
        
=======
        x -= movementSpeed ;

    if keyboard.is_pressed('d'):
        x += movementSpeed ;

    if keyboard.is_pressed('s'):
        y += movementSpeed ;

    if keyboard.is_pressed('w'):
        y -= movementSpeed ;

>>>>>>> 968e97c93ac48e9e97d0d13a947e6b2f160e5ccf

    UpdateScreen()
