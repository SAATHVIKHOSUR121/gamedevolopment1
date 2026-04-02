import pgzrun, random
WIDTH = 800
HEIGHT = 600
#actors
jerry = Actor("jerry.png")
tom = Actor("tom.png")
score = 0
gameover = False
def draw():
    #drawing the background
    screen.blit("house.jpg",(0,0))
    jerry.draw()
    tom.draw()
    #displaying text
    screen.draw.text("SCORE:"+str(score),color = "yellow",topleft = (0,0), fontsize = 50)
    if gameover == True:
        screen.fill("red")
        screen.draw.text("GAME OVER points:"+str(score), color = "yellow", center = (400, 300), fontsize = 100)
#RANDOM POSTION FOR JERRY
def ran1():
    jerry.x = random.randint(0,800)
    jerry.y = random.randint(0,600)
ran1()

def update():
    pass
    global score
    if keyboard.left:
        tom.x = tom.x - 15
    if keyboard.right:
        tom.x = tom.x + 15
    if keyboard.up:
        tom.y = tom.y - 15
    if keyboard.down:
        tom.y = tom.y + 15
    if tom.colliderect(jerry):
        score = score + 1
        ran1()
#gameover function
def gameover1():
    global gameover
    gameover = True
clock.schedule(gameover1,30.0)
pgzrun.go()
pgzrun.go()
