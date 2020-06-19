import pygame as pg
from dataclasses import dataclass

BREITE, SPALTEN, ZEILEN = 400, 10, 20
ABSTAND = BREITE // SPALTEN
HÖHE = ABSTAND * ZEILEN
grid = [0] * SPALTEN * ZEILEN

bilder = []
for n in range(8):
    bilder.append(pg.transform.scale(
        pg.image.load(f'tt3_{n}.gif'), (ABSTAND, ABSTAND)))

pg.init()
screen = pg.display.set_mode([BREITE, HÖHE])

tetrominoes = [[0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 5, 5, 5, 0, 0, 0, 5, 0, 0, 0, 0, 0],
               [0, 0, 7, 0, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 2, 2, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [4, 4, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 6, 6, 6, 0, 0, 6, 0, 0, 0, 0, 0, 0]]


@dataclass
class Tetrominoe():
	zeile : int = 0
	spalte : int = 3
	tet : list

	def show(self):
		for n, farbe in enumerate(self.tet):
			if farbe > 0:
				#position ermitteln
				y = n // 4 * ABSTAND # Y = Zeilen
				x = n % 4 * ABSTAND # X = Spalten
				

weitermachen = True

while weitermachen:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            weitermachen = False
    screen.fill((0, 0, 0))
    for n, farbe in enumerate(grid):
        if farbe > 0:
            x = n % SPALTEN * ABSTAND
            y = n // SPALTEN * ABSTAND
            screen.blit(bilder[farbe], (x, y))

    pg.display.flip()

pg.quit()
