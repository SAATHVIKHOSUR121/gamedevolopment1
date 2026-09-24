import pygame, random
pygame.init()
screen = pygame.display.set_mode((800, 500))
bg = pygame.image.load('images/mariobg.jpg')
bg = pygame.transform.scale(bg, (800, 500))
startime = pygame.time.get_ticks()
font = pygame.font.SysFont('TIMES NEW ROMAN',25)
class Mario(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/mario.png')
        self.image = pygame.transform.scale(self.image,(80,100))
        self.rect = self.image.get_rect()
        self.rect.center = [250, 250]
        self.score = 0
    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_d] and self.rect.x < 720:
            self.rect.x += 1
        if key[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= 1
        if key[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= 1 
        if key[pygame.K_s] and self.rect.y < 400:
            self.rect.y += 1
        if pygame.sprite.spritecollide(self,coingroup, True):
            self.score = self.score + 1
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/coin.png')
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.center = [random.randint(0,800), random.randint(0,500)]


        
mario1 = Mario()
charactergroup = pygame.sprite.Group()
coingroup = pygame.sprite.Group() 
charactergroup.add(mario1)

while True:
    currentime = pygame.time.get_ticks()
    screen.blit(bg, (0,0))
    text = font.render("SCORE:" + str(mario1.score),True,('black'))
    screen.blit(text,(10,10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if currentime - startime > 700:
        coin1 = Coin()
        coingroup.add(coin1)
        startime = currentime
    charactergroup.draw(screen)
    charactergroup.update()
    coingroup.draw(screen)
    pygame.display.update()