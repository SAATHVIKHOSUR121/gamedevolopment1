import random, time, pygame
pygame.init()
screen = pygame.display.set_mode((700, 650))
bg = pygame.image.load('images/forestbg.jpg')
bg = pygame.transform.scale(bg, (700, 650))
class Basket(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/fruitbasket.png') 
        self.rect = self.image.get_rect()
        self.rect.center = [350,600]
basket1 = Basket()
charactergroup = pygame.sprite.Group()
charactergroup.add(basket1)
while True:
    screen.blit(bg, (0,0))
    charactergroup.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()


