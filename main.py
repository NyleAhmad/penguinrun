import pygame
import random
import math
from pygame import mixer
pygame.init()

#music
mixer.music.load('Background_Music.mp3')
mixer.music.play(-1)
jumping_sound = mixer.Sound('jumpingsound.mp3')
pengdie_sound = mixer.Sound('penguindie.mp3')
# Game Screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Penguin")
bbypeng = pygame.image.load('newintrobackground.png')
pygame.display.set_icon(bbypeng)
introbackground = pygame.image.load('newintrobackground.png')
mainbackground = pygame.image.load('mainbackground.jpg')

WHITE = (255, 255, 255)
score = 0
all_scores = []



class Player(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		super().__init__()
		self.attack_animation = False
		self.jumpy = False
		self.sprites = []
		self.sprites.append(pygame.image.load('walk-0.png'))
		self.sprites.append(pygame.image.load('walk-1.png'))
		self.sprites.append(pygame.image.load('walk-2.png'))
		self.sprites.append(pygame.image.load('walk-3.png'))
		self.sprites.append(pygame.image.load('walk-4.png'))
		self.sprites.append(pygame.image.load('walk-5.png'))
		self.sprites.append(pygame.image.load('walk-7.png'))

		self.current_sprite = 0

		self.image = self.sprites[self.current_sprite]

		#self.rect = self.image.get_rect()
		self.mask = pygame.mask.from_surface(self.image)

		self.rect = self.image.get_rect()
		self.mask = pygame.mask.from_surface(self.image)
		self.rect.x = pos_x
		self.rect.y = pos_y
		self.vel_y = 22

	def walk(self):
		self.attack_animation = True

	def jump(self):
		jumping_sound.play()
		self.jumpy = True





	def Outrotxt():
		global smallerfont
		global score
		global all_scores
		high_score = max(all_scores)
		screen.fill((255, 255, 255))
		smallerfont = pygame.font.Font(None, 42)
		smallestfont = pygame.font.Font(None, 20)
		deadtext = smallestfont.render("You died ):", True, (0, 0, 0))
		scoretext = smallerfont.render("Score: " + str(score), True, (0, 0, 0))
		highscoretext = smallestfont.render("High Score: " + str(high_score), True, (0, 0, 0))
		screen.blit(deadtext, (screen_width / 2 - 50, screen_height / 2 - 20))
		screen.blit(scoretext, (screen_width / 2 - 75, 350))
		screen.blit(highscoretext, (screen_width / 2 - 65, 335))


	#def reset(self):
		#game_state.__init__()
	def update(self, speed):
		global game_state
		if self.attack_animation == True:
			self.current_sprite += speed
			#self.rect.x += 2

			if int(self.current_sprite) >= len(self.sprites):
				self.current_sprite = 0
				#self.attack_animation = False

		self.image = self.sprites[int(self.current_sprite)]
		if self.jumpy == True:

			self.rect.y -= self.vel_y
			self.vel_y -= 1
			if self.vel_y < -22:
				self.jumpy = False
				self.vel_y = 22





class Badguy(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		super().__init__()

		self.sprites = []
		self.sprites.append(pygame.image.load('L1E.png'))
		self.sprites.append(pygame.image.load('L2E.png'))
		self.sprites.append(pygame.image.load('L3E.png'))
		self.sprites.append(pygame.image.load('L5E.png'))
		self.sprites.append(pygame.image.load('L6E.png'))

		self.current_sprite = 0

		self.image = self.sprites[self.current_sprite]

		self.rect = self.image.get_rect()
		self.mask = pygame.mask.from_surface(self.image)
		self.rect.x = pos_x
		self.rect.y = pos_y
		self.s = 0

	def update(self, speed):

		self.current_sprite += speed
		self.rect.x -= self.s

		if int(self.current_sprite) >= len(self.sprites):
			self.current_sprite = 0

	# self.attack_animation = False

		self.image = self.sprites[int(self.current_sprite)]







class Snowball(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		super().__init__()
		self.drop_animation = True
		self.sprites = []
		self.sprites.append(pygame.image.load('pngimg.com - snowball_PNG18.png'))
		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]
		self.rect = self.image.get_rect()
		self.rect.x = pos_x
		self.rect.y = pos_y

	def drop(self):
		self.drop_animation = True

	def update(self, speed):
		if self.drop_animation == True:

			self.rect.y += 6

			if int(self.current_sprite) >= len(self.sprites):
				self.current_sprite = 0
				#self.drop_animation = False

		self.image = self.sprites[int(self.current_sprite)]


def isCollision(q, w, u, i):
	distance = math.sqrt((math.pow(q - u, 2)) + (math.pow(w - i, 2)))
	if distance < 20:
		return True
	else:
		return False

ran1 = random.randint(600, 900)
ran2 = random.randint(600, 900)
ran3 = random.randint(600, 900)
ran4 = random.randint(600, 900)
ran5 = random.randint(600, 900)
i = 0
# Creating the sprites and groups
Player_moving_sprites = pygame.sprite.Group()
bg_moving_sprites = pygame.sprite.Group()
bg2_moving_sprites = pygame.sprite.Group()
bg3_moving_sprites = pygame.sprite.Group()
bg4_moving_sprites = pygame.sprite.Group()
bg5_moving_sprites = pygame.sprite.Group()
player = Player(75, screen_height - 100)
badguy = Badguy(ran1, screen_height - 100)
badguy2 = Badguy(ran2, screen_height - 100)
badguy3 = Badguy(ran3, screen_height - 100)
badguy4 = Badguy(ran4, screen_height - 100)
badguy5 = Badguy(ran5, screen_height - 100)
badguy.s = random.randint(5, 8)
badguy2.s = random.randint(5, 8)
badguy3.s = random.randint(5, 8)
badguy4.s = random.randint(5, 8)
badguy5.s = random.randint(5, 8)

Snowball = Snowball(25, -30)

bg_moving_sprites.add(badguy)
bg2_moving_sprites.add(badguy2)
bg3_moving_sprites.add(badguy3)
bg4_moving_sprites.add(badguy4)
bg5_moving_sprites.add(badguy5)
Player_moving_sprites.add(player)
#moving_sprites.add(Snowball)
Jump = Player.jump


class GameState():
	def __init__(self):
		self.state = 'intro'


	def intro(self):

		# Set up the font
		font = pygame.font.Font(None, 92)
		smallerfont = pygame.font.Font(None, 42)
		text = font.render("Penguin Run", True, (0, 0, 0))
		text_rect = text.get_rect(center=(screen_width / 2, screen_height / 2))
		#instructions = smallerfont.render("Press SPACE to walk", True, (0, 0, 0))
		#secondinstructions = smallerfont.render("Press C to stop", True, (0, 0, 0))
		thirdinstructions = smallerfont.render("Press any KEY to continue(:", True, (0, 0, 0))
		# Set up the animation
		angle = 0
		clock = pygame.time.Clock()


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				self.state = 'main_game'

			# Draw to the screen
			screen.fill((255, 255, 255))
			screen.blit(introbackground, (-200, -300))
			angle += 1.7
			rotated_text = pygame.transform.rotate(text, angle)
			rotated_rect = rotated_text.get_rect(center=text_rect.center)
			screen.blit(rotated_text, rotated_rect)
			#screen.blit(instructions, (screen_width - 300, 25))
			#screen.blit(secondinstructions, (screen_width - 300, 60))
			screen.blit(thirdinstructions, ((screen_width/3) - 69, screen_height - 60))

			clock.tick(60)

	def main_game(self):


		global i
		global Jump
		global score
		global all_scores

		smallerfont = pygame.font.Font(None, 40)
		score_txt = smallerfont.render("Score: " + str(score), True, (0, 0, 0))
		i -= 4
		# Drawing
		screen.blit(mainbackground, (i, -200))
		screen.blit(mainbackground, (screen_width + i, -200))
		screen.blit(score_txt, (screen_width - 200, 10))
		# moving_sprites.draw(screen)
		# moving_sprites.update(0.25)
		Player_moving_sprites.draw(screen)
		Player_moving_sprites.update(0.25)
		bg_moving_sprites.draw(screen)
		bg_moving_sprites.update(0.25)
		bg2_moving_sprites.draw(screen)
		bg2_moving_sprites.update(0.25)
		bg3_moving_sprites.draw(screen)
		bg3_moving_sprites.update(0.25)
		bg4_moving_sprites.draw(screen)
		bg4_moving_sprites.update(0.25)
		bg5_moving_sprites.draw(screen)
		bg5_moving_sprites.update(0.25)



		#score
		if badguy.rect.x or badguy2.rect.x or badguy3.x or badguy4.rect.x or badguy5.rect.x >= 76:
			score += 1
			all_scores.append(score)


		player.walk()
		#Bad Guy looping
		if badguy.rect.x <= -50:
			badguy.rect.x = screen_width + 40
		if badguy2.rect.x <= -74:
			badguy2.rect.x = screen_width + 30
		if badguy3.rect.x <= -74:
			badguy3.rect.x = screen_width + 10
		if badguy4.rect.x <= -74:
			badguy4.rect.x = screen_width + 30
		if badguy5.rect.x <= -69:
			badguy5.rect.x = screen_width + 69

		#Collisions
		self.hit = isCollision(badguy.rect.x, badguy.rect.y, player.rect.x, player.rect.y)
		self.hit2 = isCollision(badguy2.rect.x, badguy2.rect.y, player.rect.x, player.rect.y)
		self.hit3 = isCollision(badguy3.rect.x, badguy3.rect.y, player.rect.x, player.rect.y)
		self.hit4 = isCollision(badguy4.rect.x, badguy4.rect.y, player.rect.x, player.rect.y)
		self.hit5 = isCollision(badguy5.rect.x, badguy5.rect.y, player.rect.x, player.rect.y)
		if self.hit:
			pengdie_sound.play()
			self.state = 'dead'
		if self.hit2:
			pengdie_sound.play()
			self.state = 'dead'
		if self.hit3:
			pengdie_sound.play()
			self.state = 'dead'
		if self.hit4:
			pengdie_sound.play()
			self.state = 'dead'
		if self.hit5:
			pengdie_sound.play()
			self.state = 'dead'



		for event in pygame.event.get():


			if event.type == pygame.QUIT:
				pygame.quit()
			if self.state == 'dead':
				break

			if event.type == pygame.KEYDOWN:
				# player jump
				if event.key == pygame.K_SPACE and player.jumpy == False:
					player.jump()




		#Background looping
		if i == -screen_width:
			screen.blit(mainbackground, (screen_width + 6 * i, -200))
			i = 0

	def dead(self):
		global score
		global high_score
		global all_scoresw

		Player.Outrotxt()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

			if event.type == pygame.KEYUP and self.state == 'dead':
				print(all_scores)
				score = 0
				badguy.rect.x = random.randint(500, 900)
				badguy2.rect.x = random.randint(500, 900)
				badguy3.rect.x = random.randint(500, 900)
				badguy4.rect.x = random.randint(500, 900)
				badguy5.rect.x = random.randint(500, 900)
				self.state = 'main_game'










	def state_manager(self):
		if self.state == 'intro':
			self.intro()

		if self.state == 'main_game':
			self.main_game()

		if self.state == 'dead':
			self.dead()


		pygame.display.update()




# General setup
clock = pygame.time.Clock()
game_state = GameState()




#Game loop
while True:
	game_state.state_manager()
	clock.tick(60)




