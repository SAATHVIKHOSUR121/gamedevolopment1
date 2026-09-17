import pygame
pygame.init()
screen = pygame.display.set_mode((800, 500))
bg = pygame.image.load('images/mariobg.jpg')
bg = pygame.transform.scale(bg, (800, 500))
class Mario(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/mario.png')
        self.image = pygame.transform.scale(self.image,(80,100))
        self.rect = self.image.get_rect()
        self.rect.center = [250, 250]

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            self.rect.x += 1
        if key[pygame.K_a]:
            self.rect.x -= 1
        if key[pygame.K_w]:
            self.rect.y -= 1 
        if key[pygame.K_s]:
            self.rect.y += 1
        
mario1 = Mario()
charactergroup = pygame.sprite.Group()
charactergroup.add(mario1)
while True:
    screen.blit(bg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    charactergroup.draw(screen)
    charactergroup.update()
    pygame.display.update()