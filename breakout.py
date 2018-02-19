import sys, pygame
from pygame.locals import *

WINWIDTH = 1280
WINHEIGHT = 720
FPS = 60

#COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

BGCOLOR = BLACK
ENEMYCOLOR = RED
PLAYERCOLOR = WHITE
BALLCOLOR = WHITE

class Brick():
	
	def __init__(self):
		self.BRICKWIDTH = 50
		self.BRICKHEIGHT = 25
		self.POSX = 0
		self.POSY = 5 
		
	def draw(self, x, y):
		pygame.draw.rect(DISPLAYSURF, RED, (x, y, self.BRICKWIDTH, self.BRICKHEIGHT))


class Ball():

	def __init__(self):
		self.BALLWIDTH = 15 
		self.BALLHEIGHT = 15 
		self.POSX = (WINWIDTH / 2) - self.BALLWIDTH
		self.POSY = WINHEIGHT - 65 
		self.BALLSPEEDX = 1 
		self.BALLSPEEDY = 1

	def draw(self):
		pygame.draw.rect(DISPLAYSURF, WHITE, (self.POSX, self.POSY, self.BALLWIDTH, self.BALLHEIGHT))

	def move(self):
		self.POSX += self.BALLSPEEDX
		self.POSY += self.BALLSPEEDY

		if self.POSX > WINWIDTH - self.BALLWIDTH or self.POSX < 0:
			self.BALLSPEEDX = self.BALLSPEEDX * -1
		if self.POSY > WINHEIGHT - self.BALLHEIGHT or self.POSY < 0:
			self.BALLSPEEDY = self.BALLSPEEDY * -1


class Player():

	def __init__(self):
		self.PLAYERWIDTH = 150
		self.PLAYERHEIGHT = 50
		self.POSX = (WINWIDTH - self.PLAYERWIDTH) / 2 
		self.POSY = (WINHEIGHT - self.PLAYERHEIGHT)
		self.MOVESPEED = 6
		self.MOVELEFT = False
		self.MOVERIGHT = False

	def draw(self):
		pygame.draw.rect(DISPLAYSURF, WHITE, (self.POSX, self.POSY, self.PLAYERWIDTH, self.PLAYERHEIGHT))

	def move(self, key):
		if key == K_LEFT:
			self.MOVERIGHT = False 
			self.MOVELEFT = True 
		if  key == K_RIGHT:
			self.MOVELEFT = False
			self.MOVERIGHT = True
	
	def stop(self, key):		
		if key == K_LEFT or K_RIGHT:
			self.MOVERIGHT = False
			self.MOVELEFT = False

	def update(self):
		if self.MOVERIGHT == True and self.POSX < (WINWIDTH - self.PLAYERWIDTH):
			self.POSX += self.MOVESPEED
		if self.MOVELEFT == True and self.POSX > 0:
			self.POSX -= self.MOVESPEED

def main():
	global FPSCLOCK, DISPLAYSURF
	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
		
	pygame.display.set_caption('Breakout Clone')
	
	brick = Brick()
	ball = Ball()
	player = Player()

	while True:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()
			
			if event.type == KEYDOWN: 
				player.move(event.key)
			if event.type == KEYUP:
				player.stop(event.key)
	
		DISPLAYSURF.fill(BGCOLOR)

		brickX = 20 
		brickY = 0
		for i in range(0, 5):
			for j in range (0, 19):
				brick.draw(brickX, brickY)
				brickX += 70
			brickX = 20 
			brickY += 50
			


		player.update()
		player.draw()
		ball.draw()
		ball.move()
		pygame.display.update()
		FPSCLOCK.tick(FPS)

if __name__ == '__main__':
	main()
