import pgzrun, random
WIDTH = 800
HEIGHT = 600
#actors
jerry = Actor("jerry.png")
tom = Actor("tom.png")
def draw():
    #drawing the background
    screen.blit("house.jpg",(0,0))
    jerry.draw()
    tom.draw()
#RANDOM POSTION FOR JERRY
def ran1():
    jerry.x = random.randint(0,800)
    jerry.y = random.randint(0,600)
ran1()
score = 0

def update():
    pass
    global score
    if keyboard.left:
        tom.x = tom.x - 1
    if keyboard.right:
        tom.x = tom.x + 1
    if keyboard.up:
        tom.y = tom.y - 1
    if keyboard.down:
        tom.y = tom.y + 1
    if tom.colliderect(jerry):
        score = score + 1
        ran1()

pgzrun.go()