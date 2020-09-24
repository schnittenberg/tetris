import pygame as pg
from dataclasses import dataclass

BREITE, SPALTEN, ZEILEN = 400, 10, 20
ABSTAND = BREITE // SPALTEN
HÖHE = ABSTAND * ZEILEN
grid = [0] * SPALTEN * ZEILEN
speed = 500
bilder = []
for n in range(8):
    bilder.append(pg.transform.scale(
        pg.image.load(f'tt3_{n}.gif'), (ABSTAND, ABSTAND)))

pg.init()
screen = pg.display.set_mode([BREITE, HÖHE])
TETROMINODOWN = pg.USEREVENT+1
SPEEDUP = pg.USEREVENT+2
pg.time.set_timer(TETROMINODOWN, speed)
pg.time.set_timer(SPEEDUP, 30_000)


tetrominoes = [[0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 5, 5, 5, 0, 0, 0, 5, 0, 0, 0, 0, 0],
               [0, 0, 7, 0, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 2, 2, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [4, 4, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 6, 6, 6, 0, 0, 6, 0, 0, 0, 0, 0, 0]]


@dataclass
class Tetrominoe():
    tet: list
    zeile: int = 0
    spalte: int = 3

    def show(self):
        for n, farbe in enumerate(self.tet):
            if farbe > 0:
                # position ermitteln
                y = (self.zeile + n // 4) * ABSTAND  # Y = Zeilen
                x = (self.spalte + n % 4) * ABSTAND  # X = Spalten
                screen.blit(bilder[farbe], (x,y))

    def update(self, zOff, sOff):
        self.zeile += zOff
        self.spalte += sOff

figur = Tetrominoe(tetrominoes[3])             


weitermachen = True
clock = pg.time.Clock()
while weitermachen:
    clock.tick(5)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            weitermachen = False
        if event.type == TETROMINODOWN:
            figur.update(1,0)
        if event.type == SPEEDUP:
            speed = int(speed * 0.8)
            pg.time.set_timer(TETROMINODOWN, 500)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                figur.update(0,-1)
            if event.key == pg.K_RIGHT:
                figur.update(0,1)
            if event.key == pg.K_DOWN:
                figur.update(1,0)
            
              
    screen.fill((0, 0, 0))
    figur.show()
    for n, farbe in enumerate(grid):
        if farbe > 0:
            x = n % SPALTEN * ABSTAND
            y = n // SPALTEN * ABSTAND
            screen.blit(bilder[farbe], (x, y))

    pg.display.flip()

pg.quit()
