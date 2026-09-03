import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
card = pygame.image.load('images/emptybirthdaycard.jpg')
card = pygame.transform.scale(card, (500,540))
font = pygame.font.SysFont("Sans Serif", 50)
text = font.render("HAPPY BIRTHDAY", True, "blue")
while True:
    screen.blit(card,(0,0))
    screen.blit(text, (100,200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()