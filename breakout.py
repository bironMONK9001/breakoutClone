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
		self.POSY = 10
		
	def draw(self):
		pygame.draw.rect(DISPLAYSURF, RED, (self.POSX, self.POSY, self.BRICKWIDTH, self.BRICKHEIGHT))


class Ball():

	def __init__(self):
		self.BALLWIDTH = 15 
		self.BALLHEIGHT = 15
		self.POSX = (WINWIDTH / 2) - self.BALLWIDTH
		self.POSY = WINHEIGHT - 65 
		self.BALLSPEED = 10
		self.UPLEFT =  True	
		self.UPRIGHT = False
		self.DOWNRIGHT = False
		self.DOWNLEFT = False

	def draw(self):
		pygame.draw.rect(DISPLAYSURF, WHITE, (self.POSX, self.POSY, self.BALLWIDTH, self.BALLHEIGHT))
	
	def update(self):
		ball = Ball()	
		ball.collide()	
		if self.UPLEFT == True:
			self.POSX -= self.BALLSPEED
			self.POSY -= self.BALLSPEED
		if self.UPRIGHT == True:
			self.POSX += self.BALLSPEED
			self.POSY -= self.BALLSPEED
		if self.DOWNLEFT == True:
			self.POSX -= self.BALLSPEED
			self.POSY += self.BALLSPEED
		if self.DOWNRIGHT == True:
			self.POSX += self.BALLSPEED
			self.POSY += self.BALLSPEED
			
	def collide(self):
		if self.POSX > (WINWIDTH - self.BALLWIDTH) or self.POSX < 0:
			if self.DOWNLEFT == True: 
				self.DOWNLEFT = False
				self.DOWNRIGHT = True
			if self.UPLEFT == True:
				self.UPLEFT = False
				self.UPRIGHT = True
			if self.DOWNRIGHT == True:
				self.DOWNRIGHT = False
				self.DOWNLEFT = True
			if self.UPRIGHT == True:
				self.UPRIGHT = False
				self.UPLEFT = True
			

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
		brick.draw()	
		player.update()
		player.draw()
		ball.update()
		ball.draw()
		pygame.display.update()
		FPSCLOCK.tick(FPS)

if __name__ == '__main__':
	main()
