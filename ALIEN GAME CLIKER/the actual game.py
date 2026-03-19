import pgzrun, random
WIDTH = 700
HEIGHT = 700
TITLE = "ALIEN GAME "
buttonstorer = Actor("big red button.png")
message = "start by clicking the button (if you can)"
def repetition():
    buttonstorer.x = random.randint(0, 700)
    buttonstorer.y = random.randint(0, 700)
    clock.schedule_unique(fail,1.0)
def fail():
    global message
    message = "Ha you missed"
    repetition()


def draw():
    screen.fill("white")
    buttonstorer.draw()
    screen.draw.text(message, center = (350, 100),fontsize = 25, color = "black" )

def update():
    pass
def on_mouse_down(pos):
    global message
    if buttonstorer.collidepoint(pos):
        message = "how did you hit that?"
        clock.unschedule(fail)
        repetition()
    else: message = "Ha you missed"
clock.schedule_interval(repetition, 1.5)
pgzrun.go()
