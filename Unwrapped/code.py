import random, pgzrun
WIDTH = 800
HEIGHT = 450
x = 0
gummy = Actor("gummy.png")

def draw():
    screen.clear()
    screen.blit("firstbg", (x,0))
    screen.blit("secondbg", (x + 800,0))
    gummy.draw()
def update():
    global x
    if keyboard.right: 
        x-= 1
    if keyboard.left:
        x+= 1
pgzrun.go()
