import pygame
pygame.init()
screen = pygame.display.set_mode((700,700))
class audi:

    def __init__(self, radius, x, y, color, width ):
        self.radius = radius
        self.x = x
        self.y = y
        self.color = color
        self.width = width
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, self.width )
lis1 = []
for i in range(4):
    audi1 = audi(70, i * 120+180,350, "black", 5 )
    lis1.append(audi1)

while True:
    screen.fill("white")
    for i in lis1:
        i.draw()
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    pygame.display.update()