import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
class Ball():
    def __init__(self, color, radius, x, y, width):
        self.color = color
        self.radius = radius
        self.x = x
        self.y = y
        self.width = width
    def drawball(self):
        pygame.draw.circle(screen, self.color,(self.x, self.y), self.radius, self.width)
    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.x += 0.05
        if key[pygame.K_LEFT]:
            self.x -= 0.05
        if key[pygame.K_UP]:
            self.y -= 0.05
        if key[pygame.K_DOWN]:
            self.y += 0.05
        if key[pygame.K_c]:
            self.color = "black"
        if key[pygame.K_r]:
            self.color = "red"

ball1 = Ball("red", 50, 250,250, 0)
while True:
    screen.fill("dark green")
    ball1.drawball()
    ball1.move()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
