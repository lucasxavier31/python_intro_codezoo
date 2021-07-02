#Jogo Space invaders - by: Codezoo
import pygame as py
import pygame
import random
import math
#inicializando o game
py.init()
py.font.init()

#criando a janela do game e definindo o tamanho
tela = py.display.set_mode((800,800))

#dando nome a janela do game e adicionando um novo icone
py.display.set_caption('Space Invaders - Codezoo')
icone = py.image.load('icone.png')
py.display.set_icon(icone)

#adicionando background - bg
bg = py.transform.scale(py.image.load('universo.png'), (800,800))

#som de fundo
pygame.mixer.music.load('som_fundo.wav')
pygame.mixer.music.play(-1)

#adicionando player
player = py.transform.scale(py.image.load('minha_nave.png'), (80,80))
posição_x = 400
posição_y = 650
posição_x_change = 0
posição_y_change = 0

#adicionando alien

alien = []
alienx = []
alieny = []
alienx_change = []
alieny_change =[]
num_alien = 6
vel = 5


for i in range(num_alien):
	alien.append(py.transform.scale(py.image.load('alien1.png'), (80,80)))
	alienx.append(random.randint(0,720))
	alieny.append(random.randint(0, 150))
	alienx_change.append (vel)
	alieny_change.append (40)

#adicionando laser

laser = py.transform.scale(py.image.load('laser.png'), (80,80))
laserX = 0
laserY = posição_y
laserX_change = 0
laserY_change = 15
laser_shoot = 'pronto'


def Player(x, y):
	tela.blit(player, (x,y))

def Alien(x, y, i):
	tela.blit(alien[i], (x,y))

def fire_laser(x,y):
	global laser_shoot
	laser_shoot = 'fire'
	tela.blit(laser, (x,y))

def Colisao(laserX, laserY, alienx, alieny):
	distance = math.sqrt((math.pow(laserX-alienx,2)+(math.pow(laserY-alieny,2))))
	if distance < 40:
		return True
	else:
		return False

# pontuação
score_value = 0
fonte = py.font.SysFont('comicsans', 40)


def Pontos(x,y):
	score = fonte.render('Pontos: ' + str(score_value), True, (0, 255,0))
	tela.blit(score, (x,y))


def Game_over():
	fonte1 = py.font.SysFont('comicsans', 100)
	fim_jogo = fonte1.render('GAME OVER', True, (255,255,255))
	tela.blit(fim_jogo, (200, 400))

#criando um loop para manter a janela aberta
clock = pygame.time.Clock()
run = True
while run:
	# possibilidade de trocar a cor de fundo
	tela.fill((0, 0, 0))
	dt = clock.tick(30)
	#adicionando movimento, colocar só para dar uma noção de como ocorre o movimento
	#posição_x += 0.2
	tela.blit(bg, (0, 0))
	#evento para quando game for fechado
	for event in py.event.get():
		if event.type == py.QUIT:
			run = False

		if event.type == pygame.KEYDOWN:

			if event.key == pygame.K_LEFT:
				posição_x_change = -10
			if event.key == pygame.K_RIGHT:
				posição_x_change = 10
			if event.key == pygame.K_SPACE:
				if laser_shoot == 'pronto':
					#laser_som = pygame.mixer.Sound('laser.wav')
					#laser_som.play()
					laserX = posição_x
					fire_laser(posição_x, laserY)

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				posição_x_change = 0

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN:
					posição_y_change = -1
			if event.key == pygame.K_UP:
					posição_y_change = 1
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
				posição_y_change = 0


	#Bordas do game
	posição_x += posição_x_change
	if posição_x <= 0:
		posição_x =0
	elif posição_x >= 720:
		posição_x = 720
	posição_y -= posição_y_change
	if posição_y <= 0:
		posição_y =0
	elif posição_y >= 720:
		posição_y = 720
#movimento alien
	for i in range(num_alien):

		#Fim de jogo
		if alieny[i] > 700:
			for j in range (num_alien):
				alieny[j] = 2000
			Game_over()
			break

		alienx[i] += alienx_change[i]
		if alienx[i] <= 0:
			alienx_change[i] = vel
			alieny[i] += alieny_change[i]
		elif alienx[i] >= 720:
			alienx_change[i] = -vel
			alieny[i] += alieny_change[i]
		# colisão
		colisao = Colisao(laserX, laserY, alienx[i], alieny[i])
		if colisao:
			explosao_som = pygame.mixer.Sound('explosao.wav')
			explosao_som.play()
			laserY = posição_y
			laser_shoot = 'pronto'
			score_value += 1
			alienx[i] = random.randint(0, 720)
			alieny[i] = random.randint(0, 150)

		Alien(alienx[i], alieny[i], i)

	#movimento do laser
	if laserY <= 0:
		laserY = posição_y
		laser_shoot = 'pronto'
	if laser_shoot == 'fire':
		fire_laser(laserX, laserY)
		laserY -= laserY_change




	Player(posição_x, posição_y)
	Pontos(10,10)

	py.display.update()