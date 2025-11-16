import pygame
import time
import random 

"""m = [[random.randint(0,1) for i in range(25)] for j in range(25)]"""

m = [[0 for i in range(50)] for j in range(50)]

"""m = [
    [0, 0, 0],
    [1, 1, 1],
    [0, 0, 0]
]"""
#try 100x100

r = len(m) 
c = len(m[0])
yearcounter = 0

CELL_SIZE = 20 
GRID_COLOR = (40, 40, 40)
ALIVE_COLOR = (0, 255, 0)
DEAD_COLOR = (0, 0, 0)
FPS = 5 


def checksurroundings(a,i,j): #Controlla i dintorni di una cella e decide se la prossima generazione di quella cella sarà viva o morta
    s = [a[x][y] 
        for x in range(i-1,i+2) 
        for y in range(j-1,j+2) 
        if 0 <= x < len(a) and 0 <= y < len(a[0])]
    if sum(s) == 3 and a[i][j] == 0:
        return 1
    elif sum(s) in [3,4] and a[i][j] == 1:
        return 1
    else:
        return 0


def newyear(m):
    global yearcounter
    yearcounter += 1
    
    rows = len(m)
    cols = len(m[0])

    s = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(checksurroundings(m, i, j))
        s.append(row)

    return s


"""def play(m):
    while sum(sum(row) for row in m) > 0:
        m =newyear(m)
        for r in m:
            print (r)
        print("a")
        if yearcounter > 100:
            print(yearcounter)
            quit()
        
    print(yearcounter)"""


def nextgeneration(m):
    return newyear(m)
    
pygame.init()
screen = pygame.display.set_mode((c*CELL_SIZE, r*CELL_SIZE))
pygame.display.set_caption("Game of Life")
clock = pygame.time.Clock()

running = True
drawing = True   

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        
        if drawing:
            if pygame.mouse.get_pressed()[0]:   # left mouse button
                x, y = pygame.mouse.get_pos()
                j = x // CELL_SIZE
                i = y // CELL_SIZE
                m[i][j] = 1

            if pygame.mouse.get_pressed()[2]:   # right mouse button
                x, y = pygame.mouse.get_pos()
                j = x // CELL_SIZE
                i = y // CELL_SIZE
                m[i][j] = 0

            # Press space to start the simulation
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                drawing = False

    
    for i in range(r):
        for j in range(c):
            color = ALIVE_COLOR if m[i][j] == 1 else DEAD_COLOR
            pygame.draw.rect(
                screen,
                color,
                (j*CELL_SIZE, i*CELL_SIZE, CELL_SIZE-1, CELL_SIZE-1)
            )

    pygame.display.flip()

    
    if not drawing:
        m = nextgeneration(m)
        clock.tick(FPS)
        print("Generations:", yearcounter)


while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    for i in range(r):
        for j in range(c):
            color = ALIVE_COLOR if m[i][j] == 1 else DEAD_COLOR
            pygame.draw.rect(
                screen,
                color,
                (j*CELL_SIZE, i*CELL_SIZE, CELL_SIZE-1, CELL_SIZE-1)
            )
    pygame.display.flip()
    m = nextgeneration(m)
    clock.tick(FPS)
    print("Generations:", yearcounter)
pygame.quit()