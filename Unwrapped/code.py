import random, pgzrun
WIDTH = 800
HEIGHT = 450
x = 0
y = 0
gummy = Actor("gummy.png")
sodacan = Actor("itemsodacan")
bottle = Actor("itembottle")
tomato = Actor("itemtomato")
head = Actor("pixalalatedhead")
def draw():
    screen.clear()
    screen.blit("firstbg", (x,0))
    screen.blit("secondbg", (x + 800,0))

    tomato.draw()
    tomato.pos = (x + 280,330)
    sodacan.draw()
    sodacan.pos = (x + 180,290) 
    bottle.draw()
    bottle.pos = (x + 440,130)
    head.draw()
    head.pos = (-160,200)


    gummy.draw()
def update():
    global x
    x-=0.5
    if keyboard.right: 
        gummy.x += 2
    if keyboard.left:
        gummy.x -= 2
    if keyboard.up:
        gummy.y -= 2
    if keyboard.down:
        gummy.y += 2
pgzrun.go()
