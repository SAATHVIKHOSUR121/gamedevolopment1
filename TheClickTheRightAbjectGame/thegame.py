import pgzrun, random
HEIGHT = 800 
WIDTH = 1300
# gaming variables
gameover = False
youwin = False
tracker = 1
levels = 10
fallingitems = []
speed = 5
listvar = ["burger.png", "cola.png", "frenchfries.png", "pizza.png", "friedchicken.png"]
targetitem = None
wrongitem = []
def draw():
    screen.blit("flyingfoodsbg.jpg", (0,0))
    if gameover:
        screen.blit("youlosebg.jpg", (0,0))
    elif youwin:
        screen.blit("youwinbg.jpg", (0,0))
    else:
        for i in fallingitems:
            i.draw()
    
    screen.draw.text("level:" + str(tracker), topleft = (0,0), fontsize = 75, color = "Black")
    screen.draw.text("CLICK THIS ITEM => "+ targetitem, topleft = (400,0), fontsize = 50) 
# function for falling items
def randomizer(extra):
    global targetitem
    actorholder = []
    global wrongitem
    targetitem = random.choice(listvar)
    wrongitem = random.choices([i for i in listvar if i != targetitem], k=extra)
    combanation = [targetitem]+wrongitem
    random.shuffle(combanation)
    # horizontal spacing
    distance = WIDTH / (len(combanation) +1)
    for u, img in enumerate( combanation):
        act = Actor(img)
        act.active = True
        act.x = (u+1.2)*distance
        act.y = random.randint(-100,0)
        actorholder.append(act)
        animate(act, duration = max(1, speed- tracker), on_finished = lambda a=act: has_fallen(a), y=HEIGHT)
    return actorholder 


def update():
    pass
    global fallingitems
    if gameover or youwin:
        return
    if len(fallingitems) == 0:
        fallingitems = randomizer(tracker)
def has_fallen(actor):
    global gameover
    if not actor.active:
        return 
    if actor.image == targetitem:
        gameover = True 
def on_mouse_down(pos):
    global gameover
    global tracker
    global fallingitems
    for object in fallingitems:
        if object.collidepoint(pos):

            for wrongobject in wrongitem:
                print(wrongobject)
                if wrongobject == object.image:
                    gameover = True
        if targetitem == object.image:

            tracker = tracker + 1
            fallingitems = randomizer(tracker)

pgzrun.go()
