from tkinter import *
import keyboard
import time
import random
import math
from PIL import ImageTk, Image


BoardSizeX = 1920
BoardSizeY = 1080

#updates in version 4: 
# Made it so size determines whether you can eat enemies or they can eat you!
#- added a death screen 
# Enemies now grow at dA/dr rate instead of r +=1 rate to match the character rate. 
# Area attribute added to the enemies class
# Added a Character Class and instantiated the main character to the variable c
# Hence, all of the character variables are now accesed via c.variable. 
# Added a camera focus to the main character



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
        self.movement = 100/self.r + self.r*.01

class character: 
    def __init__(self): 
        #character vars
        self.x = BoardSizeX/2
        self.y = BoardSizeY/2
        self.r = 10
        self.area = 3.14 * self.r ** 2



        

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

#Movement
movementSpeed = 100/c.r + c.r*.01


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
    
    time.sleep(.0001)

def DeathScreen():
    img = Image.open(r"C:\Users\Niko\Pictures\hqdefault.jpg") 
    MainScreen.image = ImageTk.PhotoImage(img)    
    MainScreen.create_image(0, 0, image=MainScreen.image, anchor='nw')  
    MainScreen.mainloop()


ScreenCenterX = BoardSizeX
ScreenCenterY = BoardSizeY




#Focus on Main Character
MainScreen.configure(xscrollincrement = movementSpeed)
MainScreen.configure(yscrollincrement = movementSpeed)

def UpdateCamera(xMove, yMove): 
    MainScreen.xview_scroll(xMove, "units")
    MainScreen.yview_scroll(yMove, "units")

 





################################################################################################################


#Main Loop
while Alive:

    #eat bit
    for i in range(0, len(bitList)):
        if bitList[i].x <= c.x + c.r and bitList[i].x >= c.x - c.r:
            if bitList[i].y <= c.y + c.r and bitList[i].y >= c.y - c.r:
                bitList[i] = bits()
                c.r += .07
                c.area = 3.14 * c.r ** 2
    

    #Update Enemy
            
    for i in range(0, len(enemyList)):
        if enemyList[i].x <= c.x + c.r and enemyList[i].x >= c.x - c.r:
            if enemyList[i].y <= c.y + c.r and enemyList[i].y >= c.y - c.r:
                if c.area > 3.14 * enemyList[i].r ** 2:
                    c.area += 3.14 * enemyList[i].r ** 2
                    c.r = math.sqrt(c.area/(3.14))
                    enemyList[i] = enemies()
                if c.area < 3.14 * enemyList[i].r ** 2:
                    Alive = FALSE 

        enemyList[i].x += ((-1)**random.randint(0,1))*enemyList[i].movement
        enemyList[i].y += ((-1)**random.randint(0,1))*enemyList[i].movement

        #enemy eats bits
        for j in range(0, len(bitList)):
            e = enemyList[i]
            if bitList[j].x <= e.x + e.r and bitList[j].x >= e.x - e.r:
                if bitList[j].y <= e.y + e.r and bitList[j].y >= e.y - e.r:
                    bitList[j] = bits()
                    e.area += 3.14 * bitList[j].r ** 2
                    e.r = math.sqrt(e.area/3.14)
  
    #movement

        

    if keyboard.is_pressed('a'):
        c.x -= movementSpeed 
        UpdateCamera(-1, 0)
        
    if keyboard.is_pressed('d'):
        c.x += movementSpeed 
        UpdateCamera(1, 0)

    if keyboard.is_pressed('w'):
        c.y -= movementSpeed 
        UpdateCamera(0, -1)

    if keyboard.is_pressed('s'):
        c.y += movementSpeed 
        UpdateCamera(0, 1)


        # Update Camera Currently In debugging Stage

    



    UpdateScreen()


DeathScreen()







