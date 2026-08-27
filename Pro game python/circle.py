import pygame, random
pygame.init()
screen = pygame.display.set_mode((500,500))

class Circle():
    def __init__(self, radius, x, y, color, width):
        self.radius = radius
        self.x = x
        self.y = y
        self.color = color
        self.width = width
    def display(self):
        print(self.radius, self.x, self.y, self.color, self.width)
    def draw(self):
        pygame.draw.circle(screen,self.color, (self.x, self.y) , self.radius, self.width)
lis1 = []
for i in range(100):
    circle1 = Circle(random.randint(20,200), random.randint(0,500),random.randint(0,500),(random.randint(0,255),random.randint(0,255),random.randint(0,255)) , random.randint(10,50))
    lis1.append(circle1)
while True:
    screen.fill("white")
    for circle1 in lis1:
        circle1.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()