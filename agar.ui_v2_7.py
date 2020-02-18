from tkinter import *
import keyboard
import time
import random
import math
from PIL import ImageTk, Image


BoardSizeX = 1920
BoardSizeY = 1080
BoardLimit = 4000



# updates in version 6: 
# Put a boundary on Movement which included the boardlimit variable. 
# Made the spawn space much larger for bit and enemies. Changed enemy count and bit count to account for the increased board size. 
# To handle the increased level of bits and enemies without the system lagging to 2 frames a second a major restructurnig of the the update screen method needed to be done. 
# To handle this a second list of tkinter screen objects was created both for bits and enemies. Then when an object needed to be updated, it was rather than every screen update. 
# to assign a bits and enemies to their respective spot in the screen a loop was created to fill the intitial lists  
# updating the list for individual items like bits when they get eaten and replaced. 
# An intialize screen method was added to draw the intial game condition





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
        
        self.x = random.randint(-BoardLimit/2, BoardLimit/2)
        self.y = random.randint(-BoardLimit/2, BoardLimit/2)
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
        
        self.x = random.randint(-BoardLimit/2, BoardLimit/2)
        self.y = random.randint(-BoardLimit/2, BoardLimit/2)
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

master.wm_title("Agar.ui")

bit = bits()


#bits
bitList = list()
for i in range(2000):
    bit = bits()
    bitList.append(bit)

#enemy
enemyList = list()
for i in range(20):
    enemy = enemies()
    enemyList.append(enemy)

# Game State
Alive = True


################################################################################################################
#Functions and their associated variables

screenBits = []
screenEnemies = []
screenCharacter = MainScreen.create_circle(MainScreen, c.x, c.y, c.r, fill = "#fb0", outline = "#DDD", width = 1)

def initializeScreen(): 
    MainScreen.delete(screenCharacter)

    print("wprlomg")
    for i in range(0, len(enemyList)): 
        enemy = enemyList[i]
        screenEnemies.append(MainScreen.create_circle(MainScreen, enemy.x, enemy.y, enemy.r, fill = enemy.color, outline = "#DDD", width = 1))

    for i in range(0, len(bitList)): 
        bit = bitList[i]
        screenBits.append(MainScreen.create_circle(MainScreen, bit.x, bit.y, bit.r, fill = bit.color, outline = "#DDD", width = 1))

def UpdateScreen():
    
    #Draw Character
    screenCharacter = MainScreen.create_circle(MainScreen, c.x, c.y, c.r, fill = "#fb0", outline = "#DDD", width = 1)

    #Draw Enemies
    for i in range(0, len(enemyList)):
        enemy = enemyList[i]
        MainScreen.delete(screenEnemies[i])
        screenEnemies[i] = MainScreen.create_circle(MainScreen, enemy.x, enemy.y, enemy.r, fill = enemy.color, outline = "#DDD", width = 1)
    
    MainScreen.update()
    
    time.sleep(.001)
    MainScreen.delete(screenCharacter)

def DeathScreen():
    img = Image.open(r"hqdefault.jpg") 
    MainScreen.image = ImageTk.PhotoImage(img)    
    MainScreen.create_image(c.x, c.y, image=MainScreen.image, anchor='nw')  
    MainScreen.mainloop()


ScreenCenterX = BoardSizeX
ScreenCenterY = BoardSizeY




#Focus on Main Character


def UpdateCamera(xMove, yMove): 
    MainScreen.configure(xscrollincrement = c.movementSpeed)
    MainScreen.configure(yscrollincrement = c.movementSpeed)
    MainScreen.xview_scroll(xMove, "units")
    MainScreen.yview_scroll(yMove, "units")
    
    
################################################################################################################


initializeScreen()

#Main Loop
while Alive:
    
    #Character eat bit
    for i in range(0, len(bitList)):
        if math.sqrt((bitList[i].x - c.x) ** 2 + (bitList[i].y - c.y) ** 2) < c.r:
            bitList[i] = bits()
            MainScreen.delete(screenBits[i])
            screenBits[i] = MainScreen.create_circle(MainScreen, bitList[i].x, bitList[i].y, bitList[i].r, fill = bit.color, outline = "#DDD", width = 1)
            c.r += .07
            c.area = 3.14 * c.r ** 2
            c.update_movementSpeed(c.r)
    

    #Update Enemy (Is character over enemy? Is enemy over Character? Death Occurs Here. Enemy Movement. Enemy Eats Bits. )
    #character overlap 
    for i in range(0, len(enemyList)):
        if math.sqrt((enemyList[i].x - c.x) ** 2 + (enemyList[i].y - c.y) ** 2) < c.r or math.sqrt((enemyList[i].x - c.x) ** 2 + (enemyList[i].y - c.y) ** 2) < enemyList[i].r :
                if c.area > 3.14 * enemyList[i].r ** 2:
                    c.area += 3.14 * enemyList[i].r ** 2
                    c.r = math.sqrt(c.area/(3.14))
                    c.update_movementSpeed(c.r)
                    enemyList[i] = enemies()
                    MainScreen.delete(screenEnemies[i])
                    screenEnemies[i] = MainScreen.create_circle(MainScreen, enemyList[i].x, enemyList[i].y, enemyList[i].r, fill = bit.color, outline = "#DDD", width = 1)
                if c.area < 3.14 * enemyList[i].r ** 2:
                    Alive = FALSE 

        #enemy movement
        if enemyList[i].moveCounter % 4 == 0:
            enemyList[i].moveDirection[0] = ((-1)**random.randint(0,1))
            enemyList[i].moveDirection[1] = ((-1)**random.randint(0,1))

        enemyList[i].moveCounter += 1

        if enemyList[i].x > -BoardLimit/2 and enemyList[i].x < BoardLimit/2:
            enemyList[i].x += enemyList[i].moveDirection[0] * enemyList[i].movementSpeed

        if enemyList[i].y > -BoardLimit/2 and enemyList[i].y < BoardLimit/2:
            enemyList[i].y += enemyList[i].moveDirection[1] * enemyList[i].movementSpeed
        

        #enemy eats bits
        for j in range(0, len(bitList)):
            e = enemyList[i]
            if math.sqrt((bitList[j].x - e.x) ** 2 + (bitList[j].y - e.y) ** 2) < e.r:
                e.area += 3.14 * bitList[j].r ** 2
                e.r = math.sqrt(e.area/3.14)
                e.update_movementSpeed(e.r)
                bitList[j] = bits()
                MainScreen.delete(screenBits[j])
                screenBits[j] = MainScreen.create_circle(MainScreen, bitList[j].x, bitList[j].y, bitList[j].r, fill = bit.color, outline = "#DDD", width = 1)
  
    #movement

        

    if keyboard.is_pressed('a') and c.x > -.5 * BoardLimit:
        c.x -= c.movementSpeed 
        UpdateCamera(-1, 0)
        
    if keyboard.is_pressed('d') and c.x < .5 * BoardLimit:
        c.x += c.movementSpeed 
        UpdateCamera(1, 0)

    if keyboard.is_pressed('w') and c.y > -.5 * BoardLimit:
        c.y -= c.movementSpeed 
        UpdateCamera(0, -1)

    if keyboard.is_pressed('s')and c.y < .5 * BoardLimit:
        c.y += c.movementSpeed 
        UpdateCamera(0, 1)


    UpdateScreen()


DeathScreen()







