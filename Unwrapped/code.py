import random, pgzrun
WIDTH = 800
HEIGHT = 450
x = 0
y = 0
screenx = 430
screen1 = Actor("firstbg", (screenx,225))
screen2 = Actor("secondbg", (screenx,225))
gummy = Actor("gummy.png")
gummy.pos=(80,200)
sodacan = Actor("itemsodacan")
sodacan.pos= (100,290)
bottle = Actor("itembottle")
tomato = Actor("itemtomato")
head = Actor("pixalalatedhead")
scooter = Actor("scooter")
money = Actor("moneybag")
box = Actor("box")

itemslist = [sodacan, bottle, tomato, scooter, box, money]
score = 0
gameover = False
poslist = [[150,90], [320,250], [-110,320],[300,375], [80,30], [100,100]]
#poslist = [[100,290], [100, 130], [100, 350]]
def draw():
    if gameover == True:
        screen.blit("lose.jpg", (0,0))
        return
    screen.clear()
    screen1.draw()
    screen1.pos = (screenx,225)
    screen2.draw()
    screen2.pos = (screenx,225)
    head.draw()
    head.pos = (-150,200) 
    print(len(itemslist))

    for i in range(len(itemslist)):
        itemslist[i].pos = (screenx + poslist[i][0],poslist[i][1])
        itemslist[i].draw()



    gummy.draw()
    
def update():
    print("update",len(itemslist))
    global x, score, gameover, screenx
    #screenx-=0.5
    #x-=0.5
    if keyboard.right: 
        gummy.x += 2
    if keyboard.left:
        gummy.x -= 2
    if keyboard.up:
        gummy.y -= 2
    if keyboard.down:
        gummy.y += 2
    for item in itemslist:
       
        '''if gummy.colliderect(item):
            score = score + 1 
            print(score)
            
            poslist.remove(poslist[itemslist.index(item)])
            itemslist.remove(item)'''
    #if gummy.colliderect(screen2) and score != 3:
       # gameover = True


        
pgzrun.go()
