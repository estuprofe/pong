import pygame


#Variable
WIDTH = 1200
HEIGHT = 600
BORDER = 20

VELOCITY = 1

#Dibujar el escenario

pygame.init()
fgColor=pygame.Color("white")
bgColor=pygame.Color("black")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
# definición de clases
class Pelota:
    RADIUS = 15
    def __init__(self, x, y, colour, vx, vy):
        self.x = x
        self.y = y
        self.colour = colour
        self.vx = vx
        self.vy = vy

    def mostrar(self, colour):
        global screen#Para que coja la variable global
        self.colour= colour
        pygame.draw.circle(screen, self.colour,(self.x, self.y),self.RADIUS)

    def actualizar(self):

        
        
        newx = self.x + self.vx
        newy = self.y + self.vy

        if newx < BORDER+self.RADIUS:
            self.vx = -self.vx
        elif newy < BORDER+self.RADIUS or newy > HEIGHT-BORDER-self.RADIUS:
            self.vy = -self.vy
        else:
            self.mostrar(bgColor)
            self.x= self.x + self.vx
            self.y= self.y + self.vy
            self.mostrar(fgColor)
        

class Raqueta:
    WIDTH = 20
    HEIGHT = 100

    def __init__(self, y):
        self.y = y

    def show(self, colour):
        global screen, fgColor, bgColor
        pygame.draw.rect(screen, colour, pygame.Rect((WIDTH-self.WIDTH, self.y-self.HEIGHT//2, WIDTH,self.yself.HEIGHT )))

    def update(self):
        self.show(bgColor)
        self.y = pygame.mouse.get_pos()[1]
        self.show(fgColor)

#Crear objetos
pelota = Pelota(WIDTH-Pelota.RADIUS,HEIGHT//2,fgColor, -VELOCITY, -VELOCITY)
raqueta = Raqueta(HEIGHT//2)

#Bordes del juego
pygame.draw.rect(screen, fgColor, pygame.Rect(0,0,WIDTH,BORDER))
pygame.draw.rect(screen, fgColor, pygame.Rect(0,0,BORDER,WIDTH))
pygame.draw.rect(screen, fgColor, pygame.Rect(0,HEIGHT-BORDER,WIDTH, HEIGHT))
#Mostrar pantalla

#Bucle principal
while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break
    pygame.display.flip()
    pelota.actualizar()
    raqueta.update()
    
pygame.quit()
