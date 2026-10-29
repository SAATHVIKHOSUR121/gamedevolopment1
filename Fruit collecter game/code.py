import random, time, pygame
pygame.init()
screen = pygame.display.set_mode((700, 650))
bg = pygame.image.load('images/forestbg.jpg')
bg = pygame.transform.scale(bg, (700, 650))
starttime = pygame.time.get_ticks()
currenttime = pygame.time.get_ticks()
fruits = ['images/pear.png', 'images/orange.png', 'images/banana.png','images/apple.png']
clock = pygame.time.Clock()
class Basket(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/fruitbasket.png') 
        self.rect = self.image.get_rect()
        self.rect.center = [350,600]
    
    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.rect.x-=1
        if key[pygame.K_d]:
            self.rect.x+=1
class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(random.choice(fruits))
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.center = [random.randint(20,650), 0]
    def update(self):
        self.rect.y+=1
fruitgroup = pygame.sprite.Group()


basket1 = Basket()
charactergroup = pygame.sprite.Group()
charactergroup.add(basket1)
while True:
    clock.tick(200)
    currenttime = pygame.time.get_ticks()
    screen.blit(bg, (0,0))
    charactergroup.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    charactergroup.update()
    if currenttime - starttime > 500:
        fruit1 = Fruit()
        fruitgroup.add(fruit1)
        starttime = currenttime
    fruitgroup.draw(screen)
    fruitgroup.update()
    pygame.display.update()






