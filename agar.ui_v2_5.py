from tkinter import *
import keyboard
import time
import random
import math
from PIL import ImageTk, Image


BoardSizeX = 1920
BoardSizeY = 1080

# updates in version 5: 
# Added a better enemy movement system. - added enemies variable movecounter and move direction. modified movement handling in the main while loop. 
# moved movement speed into character and enemies classes for individual movement speed based off of object radius. 
# updated screen movement to more accurately match character movement 




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
        self.r = 4



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
        self.area = 3.14 * self.r ** 2
        self.moveCounter = 0
        self.movementSpeed = 100/self.r + self.r*.01
        self.moveDirection = [0,0]

    def update_movementSpeed(self, r): 
        self.movementSpeed = 100/r + r*.01

class character: 
    def __init__(self): 
        #character vars
        self.x = BoardSizeX/2
        self.y = BoardSizeY/2
        self.r = 10
        self.area = 3.14 * self.r ** 2
        self.movementSpeed = 100/self.r + self.r*.01

    def update_movementSpeed(self, r): 
        self.movementSpeed = 100/r + r*.01




        

################################################################################################################



#Miscellanious Variables

c = character() #Main Character

master = Tk()

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
for i in range(500):
    bit = bits()
    bitList.append(bit)

#enemy
enemyList = list()
for i in range(10):
    enemy = enemies()
    enemyList.append(enemy)

# Game State
Alive = True




################################################################################################################
#Functions
        
def UpdateScreen():
    #Screen
    MainScreen.delete("all")

    #Draw Character
    MainScreen.create_circle(MainScreen, c.x, c.y, c.r, fill = "#fb0", outline = "#DDD", width = 1)

    #Draw Bits
    for i in range(0, len(bitList)):
        bit = bitList[i]
        
        MainScreen.create_circle(MainScreen, bit.x, bit.y, bit.r, fill = bit.color, outline = "#DDD", width = 1)
        
    #Draw Enemies
    for i in range(0, len(enemyList)):
        enemy = enemyList[i]
        
        MainScreen.create_circle(MainScreen, enemy.x, enemy.y, enemy.r, fill = enemy.color, outline = "#DDD", width = 1)
    
    MainScreen.update()
    
    time.sleep(.001)

def DeathScreen():
    img = Image.open(r"C:\Users\Niko\Pictures\hqdefault.jpg") 
    MainScreen.image = ImageTk.PhotoImage(img)    
    MainScreen.create_image(c.x, c.y, image=MainScreen.image, anchor='nw')  
    MainScreen.mainloop()


ScreenCenterX = BoardSizeX
ScreenCenterY = BoardSizeY




#Focus on Main Character
MainScreen.configure(xscrollincrement = c.movementSpeed)
MainScreen.configure(yscrollincrement = c.movementSpeed)

def UpdateCamera(xMove, yMove): 
    #MainScreen.xview = c.x
    #MainScreen.yview = c.y 
    MainScreen.xview_scroll(xMove, "units")
    MainScreen.yview_scroll(yMove, "units")
    print(MainScreen.yview)
    

 

################################################################################################################


#Main Loop
while Alive:

    #Character eat bit
    for i in range(0, len(bitList)):
        if bitList[i].x <= c.x + c.r and bitList[i].x >= c.x - c.r:
            if bitList[i].y <= c.y + c.r and bitList[i].y >= c.y - c.r:
                bitList[i] = bits()
                c.r += .07
                c.area = 3.14 * c.r ** 2
                c.update_movementSpeed(c.r)
    

    #Update Enemy (Is character over enemy? Is enemy over Character? Death Occurs Here. Enemy Movement. Enemy Eats Bits. )
    #character overlap 
    for i in range(0, len(enemyList)):
        if enemyList[i].x <= c.x + c.r and enemyList[i].x >= c.x - c.r:
            if enemyList[i].y <= c.y + c.r and enemyList[i].y >= c.y - c.r:
                if c.area > 3.14 * enemyList[i].r ** 2:
                    c.area += 3.14 * enemyList[i].r ** 2
                    c.r = math.sqrt(c.area/(3.14))
                    c.update_movementSpeed(c.r)
                    enemyList[i] = enemies()
                if c.area < 3.14 * enemyList[i].r ** 2:
                    Alive = FALSE 

        #enemy movement
        if(enemyList[i].moveCounter % 4 == 0):
            enemyList[i].moveDirection[0] = ((-1)**random.randint(0,1))
            enemyList[i].moveDirection[1] = ((-1)**random.randint(0,1))

        enemyList[i].moveCounter += 1
        enemyList[i].x += enemyList[i].moveDirection[0] * enemyList[i].movementSpeed
        enemyList[i].y += enemyList[i].moveDirection[1] * enemyList[i].movementSpeed

        #enemy eats bits
        for j in range(0, len(bitList)):
            e = enemyList[i]
            if bitList[j].x <= e.x + e.r and bitList[j].x >= e.x - e.r:
                if bitList[j].y <= e.y + e.r and bitList[j].y >= e.y - e.r:
                    bitList[j] = bits()
                    e.area += 3.14 * bitList[j].r ** 2
                    e.r = math.sqrt(e.area/3.14)
                    e.update_movementSpeed(e.r)
  
    #movement

        

    if keyboard.is_pressed('a'):
        c.x -= c.movementSpeed 
        UpdateCamera(-1, 0)
        
    if keyboard.is_pressed('d'):
        c.x += c.movementSpeed 
        UpdateCamera(1, 0)

    if keyboard.is_pressed('w'):
        c.y -= c.movementSpeed 
        UpdateCamera(0, -1)

    if keyboard.is_pressed('s'):
        c.y += c.movementSpeed 
        UpdateCamera(0, 1)


    UpdateScreen()


DeathScreen()







