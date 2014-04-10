import pygame

class button(object):
	def __init__(self, x, y, a, b):
		self.x = x
		self.y = y
		self.a = a
		self.b = b
		self.new_button_rec = pygame.Rect(self.x, self.y, self.a, self.b)
		self.new_button_su = pygame.Surface([self.a, self.b])


if __name__=="__main__":
	pygame.init()
	main_screen = pygame.display.set_mode((600, 600))
	main_screen.fill((255, 255, 255))
	m = button(100, 100, 40, 40)
	main_screen.blit(m.new_button_su, m.new_button_rec) 
	while True:
		ev = pygame.event.poll()
		if ev.type == pygame.MOUSEBUTTONDOWN:
			x1, y1 = ev.pos
			if m.new_button_rec.collidepoint(x1, y1):
				print "clicked"
		pygame.display.flip()

		
