import random, pgzrun, time
WIDTH = 800
HEIGHT = 500
#variables for the game
satalitelis = []
lineslis = []
totalsatalites = 10
startime = 0
totalime = 0
endtime = 0
nextsatalitecounter = 0
# Function for satalites
def satafun():
    global startime
    for i in range(totalsatalites):
        satalite = Actor("thesatalite.png")
        satalite.x = random.randint(50,750)
        satalite.y = random.randint(50,450)
        satalitelis.append(satalite)
    startime = time.time()
def draw():
    global totaltime
    screen.blit("spacebg.jpg", (0,0))
    sequence = 1
    for v in satalitelis:
        v.draw()
        screen.draw.text(str(sequence),(v.pos[0], v.pos[1]+20),color = "Yellow") 
        sequence = sequence + 1
    for i in lineslis:
        screen.draw.line(i[0], i[1], color = "white" )
    if nextsatalitecounter < totalsatalites:
        totaltime = time.time() - startime  
        screen.draw.text(str(round(totaltime,1)),(10,10), color = "black")
    else: 
        screen.draw.text(str(round(totalime,2)),(10,10), color = "Yellow")

# function for mouse click
def on_mouse_down(pos):
    global nextsatalitecounter, lineslis
    if nextsatalitecounter < totalsatalites:
        if satalitelis[nextsatalitecounter].collidepoint(pos):
            if nextsatalitecounter:
                lineslis.append((satalitelis[nextsatalitecounter-1].pos, satalitelis[nextsatalitecounter].pos))
            nextsatalitecounter = nextsatalitecounter+1
        else : 
            lineslis = []
            nextsatalitecounter = 0



def update():
    pass
satafun()
pgzrun.go()
pgzrun.go()
