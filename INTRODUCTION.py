import pgzrun,random
#screen size
WIDTH = 500
HEIGHT = 500
#Main function
def draw():
    red = 255
    green = 0
    blue = random.randint(0,255)
    width = 500
    height = 250
    screen.fill("white")
    for i in range(50):
        rectangle = Rect((250,250),(width,height))
        rectangle.center = (250,250)
        screen.draw.rect(rectangle,(red, blue, green))
        width-= 5
        height+= 5
        red-= 3
        green+= 3


#Update function
def update():
    pass



#Holding the output screen
pgzrun.go()
