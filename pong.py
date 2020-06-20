# coding=utf-8
#!/bin/python3
import pygame
#from sklearn.neighbors import KNeighborsRegressor
#import pandas


<<<<<<< HEAD

# CONFIGURACIÓN
clock = pygame.time.Clock()
datos = open
=======
# Variable
>>>>>>> 4b9b44520a6e9cbffd4f6986d689c6d5c6d5e60a
WIDTH = 1200
HEIGHT = 600
BORDER = 20
COLECTA_DATOS=0
if COLECTA_DATOS:

<<<<<<< HEAD
    archivo = open("datos.csv", "w")
    archivo.write("x,y,vx,vy, raqueta.y \n")

=======
>>>>>>> 4b9b44520a6e9cbffd4f6986d689c6d5c6d5e60a
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
<<<<<<< HEAD
    
=======
>>>>>>> 4b9b44520a6e9cbffd4f6986d689c6d5c6d5e60a
    global bgColor, funcionando

    def __init__(self, x, y, colour, vx, vy):
        self.x = x
        self.y = y
        self.colour = colour
        self.vx = vx
        self.vy = vy
        self.vidas = 2

    def mostrar(self, colour):
        global screen  # Para que coja la variable global
        self.colour = colour
        

        
        
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.RADIUS)

    def actualizar(self):

        newx = self.x + self.vx
        newy = self.y + self.vy
        pygame.draw.rect(screen, bgColor, pygame.Rect(
            (BORDER,BORDER,500,100)))
<<<<<<< HEAD
        textsurface = myfont.render(f"VIDAS RESTANTES {self.vidas}", False, (220, 220, 220))
=======
        textsurface = myfont.render(f"newx {self.x} - newy {self.y}- vx {self.vx}- vy {self.vy}", False, (220, 220, 220))
>>>>>>> 4b9b44520a6e9cbffd4f6986d689c6d5c6d5e60a
        screen.blit(textsurface,(BORDER,BORDER))
        
        if newx < BORDER + self.RADIUS:
            self.vx = -self.vx
        elif newy < BORDER + self.RADIUS or newy > HEIGHT - BORDER - self.RADIUS:
            self.vy = -self.vy
        
<<<<<<< HEAD
        elif newx > WIDTH-raqueta.WIDTH and newx < WIDTH and newy > raqueta.y and newy < raqueta.y+raqueta.HEIGHT:
            temporal=self.vx
            #self.vx=0
            #self.x = WIDTH-raqueta.WIDTH-pelota.RADIUS*2
            self.vx = -abs(temporal)
        elif newx > WIDTH-raqueta.WIDTH:
            self.x = WIDTH-raqueta.WIDTH-self.RADIUS
            self.vx = -self.vx
            self.vidas = self.vidas - 1
            pygame.draw.rect(screen, bgColor, pygame.Rect(
            (BORDER,BORDER,500,100)))
            textsurface = myfont.render(f"VIDAS RESTANTES {self.vidas}", False, (220, 220, 220))
            
        
=======
        elif newx > WIDTH-raqueta.WIDTH and newy > raqueta.y and newy < raqueta.y+raqueta.WIDTH:
            self.x = WIDTH-raqueta.WIDTH-pelota.RADIUS
            self.vx = -abs(self.vx)
            
>>>>>>> 4b9b44520a6e9cbffd4f6986d689c6d5c6d5e60a
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
        

    def show(self, colour):
        global screen, fgColor, bgColor
        pygame.draw.rect(screen, colour, pygame.Rect(
            (WIDTH - self.WIDTH, self.y, self.WIDTH, self.HEIGHT)))

    def update(self):
        self.show(bgColor)
        raton = pygame.mouse.get_pos()[1]
<<<<<<< HEAD
        
=======
>>>>>>> 4b9b44520a6e9cbffd4f6986d689c6d5c6d5e60a
        if raton < BORDER or raton > HEIGHT - BORDER - self.HEIGHT:
            self.y = self.y
        else:
            self.y = raton
        self.show(fgColor)


# Crear objetos
<<<<<<< HEAD
pelota = Pelota(WIDTH // 2, HEIGHT //
                2, fgColor, -VELOCITY, -VELOCITY)
raqueta = Raqueta(HEIGHT // 2)

# Bordes del juego
pygame.draw.rect(screen, fgColor, pygame.Rect(0, 0, WIDTH, BORDER))
pygame.draw.rect(screen, fgColor, pygame.Rect(0, 0, BORDER, WIDTH))
pygame.draw.rect(screen, fgColor, pygame.Rect(
    0, HEIGHT - BORDER, WIDTH, HEIGHT))
# Mostrar pantalla

# IA
#datos = pandas.read_csv("datos.csv")
#datos = datos.drop_duplicates()

#X = datos.drop(columns='raqueta.y')
#y = datos['raqueta.y']

#clf = KneigborsRegressor (n_neighbors = 3)
#clf = clf.fit(X, y)

#df = pandas.DataFrame(columns=['x', 'y', 'vx', 'vy'])
# Bucle principal

while funcionando:
    e = pygame.event.poll()
    clock.tick(2000)
    if e.type == pygame.QUIT or pelota.vidas == 0:
        
        pygame.draw.rect(screen, fgColor, pygame.Rect(
            (0,0,WIDTH,HEIGHT)))
        textoFinal = myfont.render(f"fin de la partida, gracias por jugar", False, bgColor)
        screen.blit(textoFinal,(400,300))
        
        
        pygame.display.flip()
        pygame.time.wait(2000)
        funcionando=False
    if COLECTA_DATOS:
        archivo.write(f"{pelota.x}, {pelota.y}, {pelota.vx}, {pelota.vy}, {raqueta.y} \n")
=======
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
>>>>>>> 4b9b44520a6e9cbffd4f6986d689c6d5c6d5e60a
    pygame.display.flip()
    #toPredict = df.append({'x': pelota.x, 'y' : pelota.y, 'vx' : pelota.vx, 'vy' : pelota.vy}, ignore_index=True)
    #shouldMove = clf.predict(toPredict)

    pelota.actualizar()
    raqueta.update()

pygame.quit()
