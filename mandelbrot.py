try:
	import pygame, math, os
	from pygame.locals import *
except ImportError:
	print("Erreur d'importation des bibliotèques additionnelles")
else:
	
	def mandelbrot(re, im, max_iterations, x, y, color, screen):
		z = [0, 0]
		c = [re, im]
		n = 0
		while math.sqrt(z[0]**2+z[1]**2) < 2 and n <= max_iterations:
			n+=1
			zn = [z[0]**2-z[1]**2+c[0], 2*z[0]*z[1]+c[1]]
			z = list(zn)

		if n > max_iterations:
			video.set_at((x, y), color)
		else:
			video.set_at((x, y), ((3*n)%256, n%256, (10*n)%256))

	def calc(X, Y, screen, video,color,max_iterations):
		liste = []
		for y in range(screen[1]):
			for x in range(screen[0]):
				x1 = (x * (X[1]-X[0])/screen[0]+X[0])
				y1 = (y * (Y[0]-Y[1])/screen[1]+Y[1])
				mandelbrot(x1, y1, max_iterations, x, y, color, video)

	BLACK, WHITE, RED, GREEN, BLUE = (0,0,0), (255,255,255), (255,0,0), (0,255,0),  (0,0,255)
	pygame.init()
	WINDOW_SIZE = (1280,720)
	FPS = 120
	clock = pygame.time.Clock()
	SCREEN_SIZE = (pygame.display.Info().current_w, pygame.display.Info().current_h)
	SCREEN_POS = (SCREEN_SIZE[0]-WINDOW_SIZE[0])//2, (SCREEN_SIZE[1]-WINDOW_SIZE[1])//2
	os.environ["SDL_VIDEO_WINDOW_POS"] = f"{SCREEN_POS[0]},{SCREEN_POS[1]}"
	video = pygame.display.set_mode(WINDOW_SIZE, pygame.HWACCEL)
	pygame.display.set_caption("MANDELBROT SET")
	video.fill(WHITE)
	pygame.display.update()
	X, Y = [-2, 0.5], [-1.25, 1.25]
	MAX_ITERATIONS = 50
	calc(X,Y,WINDOW_SIZE,video,BLACK,MAX_ITERATIONS)



	started = True
	while started:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				started = False
		pygame.display.update()
	pygame.quit()
