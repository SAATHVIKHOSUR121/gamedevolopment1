import random, time, pygame
pygame.init
screen = pygame.display.set_mode((800, 700))
bg = pygame.image.load('images/bg.jpg')
bg = pygame.transform.scale(bg, (800, 700))
score = 0
clock = pygame.time.Clock()
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
flappy1 = Flappy()
flappygroup = pygame.sprite.Group()
flappygroup.add(flappy1)

while True:
    clock.tick(170)
    screen.blit(bg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    flappygroup.draw(screen)
    flappygroup.update()
    pygame.display.update()
