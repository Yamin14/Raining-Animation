import pygame
import random
pygame.init()

width, height = 720, 720
screen = pygame.display.set_mode(( width, height))

running = True

#colours
red = (255, 0, 0)
green = (0, 170, 0)
blue = (0, 0, 255)
orange = (200, 145, 0)
magenta = (255, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
grey = (140, 140, 140)
dark_grey = (70, 70, 70)
cyan = (0, 245, 245)
yellow = (255, 255, 0)

#rain drops
count = 0
j = 0
drops = []
x, y = [random.randint(0, width)], [100]
speed = 10

while running:
	screen.fill(white)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	#border
	pygame.draw.line(screen, black, (0, height), (width, height), 2)
	
	#ground
	pygame.draw.line(screen, black, (0, height-50), (width, height-50), 3)
	
	#cloud
	pygame.draw.rect(screen, grey, (0, 0, width, 50))
	z = 0
	for i in range(15):
		pygame.draw.circle(screen, grey, (z, 50), 50)
		z += 50
		
	#rain drops
	if j%3 == 0:
		count += 1
		x.append(random.randint(0, width))
		y.append(100)
		
	for i in range(count):
		if y[i]+20 <= height-50:
			pygame.draw.line(screen, cyan, (x[i], y[i]), (x[i], y[i]+20), 4)
			y[i] += speed

	j += 1
	pygame.display.flip()

pygame.quit()
