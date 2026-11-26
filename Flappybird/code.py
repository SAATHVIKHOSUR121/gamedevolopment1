import random, time, pygame
pygame.init
screen = pygame.display.set_mode((800, 700))
bg = pygame.image.load('images/bg.jpg')
bg = pygame.transform.scale(bg, (800, 700))
score = 0
clock = pygame.time.Clock()
currenttime = pygame.time.get_ticks()
startime = pygame.time.get_ticks()
class Flappy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/flappy1.png')
        self.image = pygame.transform.scale(self.image, (120,85))
        self.rect = self.image.get_rect()
        self.rect.center = [100,350]
    def update(self):
        global score
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.rect.y-=5
        self.rect.y+=1
class Pipe(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/pipe.png')
        self.image = pygame.transform.scale(self.image, (170,400))
        self.rect = self.image.get_rect()
        self.rect.center = [800, random.randint(600,650)]

    def update(self):
        self.rect.x-=3
class PipeD(pygame.sprite.Sprite):
    def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('images/pipedown.png')
            self.image = pygame.transform.scale(self.image, (170, 400))
            self.rect = self.image.get_rect()
            self.rect.center = [800, random.randint(-50, 50)]

    def update(self):
        self.rect.x-=3
pipe1 = Pipe()
pipegroup = pygame.sprite.Group()
pipegroup.add(pipe1)

flappy1 = Flappy()
flappygroup = pygame.sprite.Group()
flappygroup.add(flappy1)


while True:
    currenttime = pygame.time.get_ticks()
    clock.tick(170)
    screen.blit(bg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    flappygroup.draw(screen)
    flappygroup.update()
    pipegroup.draw(screen)
    pipegroup.update()
    if currenttime - startime > 1100:
        pipe1 = Pipe()
        pipe1d = PipeD()
        pipegroup.add(pipe1)
        pipegroup.add(pipe1d)
        startime  = currenttime


    pygame.display.update()
