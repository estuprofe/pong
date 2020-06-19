# coding=utf-8
#!/bin/python3
import pygame


# CONFIGURACIÓN


WIDTH = 1200
HEIGHT = 600
BORDER = 20

VELOCITY = 1
funcionando=True
# Dibujar el escenario

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

fgColor = pygame.Color("white")
bgColor = pygame.Color("black")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.mouse.set_visible(False)
# definición de clases


class Pelota:
    RADIUS = 15
    global bgColor, funcionando

    def __init__(self, x, y, colour, vx, vy):
        self.x = x
        self.y = y
        self.colour = colour
        self.vx = vx
        self.vy = vy

    def mostrar(self, colour):
        global screen  # Para que coja la variable global
        self.colour = colour
        

        
        
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.RADIUS)

    def actualizar(self):

        newx = self.x + self.vx
        newy = self.y + self.vy
        pygame.draw.rect(screen, bgColor, pygame.Rect(
            (BORDER,BORDER,500,100)))
        textsurface = myfont.render(f"newx {self.x} - newy {self.y}- vx {self.vx}- vy {self.vy}", False, (220, 220, 220))
        screen.blit(textsurface,(BORDER,BORDER))
        
        if newx < BORDER + self.RADIUS:
            self.vx = -self.vx
        elif newy < BORDER + self.RADIUS or newy > HEIGHT - BORDER - self.RADIUS:
            self.vy = -self.vy
        
        elif newx > WIDTH-raqueta.WIDTH and newy > raqueta.y and newy < raqueta.y+raqueta.HEIGHT:
            temporal=self.vx
            self.vx=0
            self.x = WIDTH-raqueta.WIDTH-pelota.RADIUS*2
            self.vx = -abs(temporal)
        elif newx > WIDTH-raqueta.WIDTH:
            self.x = WIDTH+BORDER+self.RADIUS
            funcionando=False
            
        else:
            self.mostrar(bgColor)
            self.x = self.x + self.vx
            self.y = self.y + self.vy
            self.mostrar(fgColor)


class Raqueta:
    WIDTH = 20
    HEIGHT = 100

    def __init__(self, y):
        self.y = y
        self.vy=0

    def show(self, colour):
        global screen, fgColor, bgColor
        pygame.draw.rect(screen, colour, pygame.Rect(
            (WIDTH - self.WIDTH, self.y, self.WIDTH, self.HEIGHT)))

    def update(self):
        self.show(bgColor)
        raton = pygame.mouse.get_pos()[1]
        if raton < BORDER or raton > HEIGHT - BORDER - self.HEIGHT:
            self.y = self.y
        else:
            self.y = raton
        self.show(fgColor)


# Crear objetos
pelota = Pelota(WIDTH - Pelota.RADIUS, HEIGHT //
                2, fgColor, -VELOCITY, -VELOCITY)
raqueta = Raqueta(HEIGHT // 2)

# Bordes del juego
pygame.draw.rect(screen, fgColor, pygame.Rect(0, 0, WIDTH, BORDER))
pygame.draw.rect(screen, fgColor, pygame.Rect(0, 0, BORDER, WIDTH))
pygame.draw.rect(screen, fgColor, pygame.Rect(
    0, HEIGHT - BORDER, WIDTH, HEIGHT))
# Mostrar pantalla

# Bucle principal
while funcionando:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        funcionando=False
    
 
    pygame.display.flip()
    pelota.actualizar()
    raqueta.update()

pygame.quit()
