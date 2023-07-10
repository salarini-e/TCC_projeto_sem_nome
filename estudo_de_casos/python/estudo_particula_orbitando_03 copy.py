import pygame
import math

# Inicializar o Pygame
pygame.init()

# Configurar a janela
window_width, window_height = 400, 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Partícula Orbitando em Canvas")

# Definir as cores
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Definir as propriedades das partículas
particle1 = {
  'x': window_width / 2,    # Posição X da partícula 1
  'y': window_height / 2,   # Posição Y da partícula 1
  'radius': 20,             # Raio da partícula 1
  'speed': 0.03,            # Velocidade de rotação da partícula 1
  'angle': 0                # Ângulo inicial da partícula 1
}

particle2 = {
  'x': window_width / 2,    # Posição X da partícula 2
  'y': window_height / 2,   # Posição Y da partícula 2
  'radius': 10,             # Raio da partícula 2
  'speed': 0.1,             # Velocidade de rotação da partícula 2
  'angle': 0                # Ângulo inicial da partícula 2
}

trail_points = []  # Lista para armazenar os pontos do rastro
max_trail_points = 150  # Número máximo de pontos do rastro

clock = pygame.time.Clock()

def draw():
  # Preencher a janela com a cor de fundo
  window.fill((255, 255, 255))

  # Calcular as novas posições das partículas
  particle1['x'] = window_width / 2 + math.cos(particle1['angle']) * 100
  particle1['y'] = window_height / 2 + math.sin(particle1['angle']) * 100

  particle2['x'] = particle1['x'] + math.cos(particle2['angle']) * 50
  particle2['y'] = particle1['y'] + math.sin(particle2['angle']) * 50

  # Adicionar o ponto atual à lista do rastro
  trail_points.append((particle2['x'], particle2['y']))

  # Limitar o número de pontos do rastro
  if len(trail_points) > max_trail_points:
    trail_points.pop(0)

  # Desenhar o rastro da partícula 2
  for i, point in enumerate(trail_points):
    color = (210, 210, 210)
    pygame.draw.circle(window, color, (int(point[0]), int(point[1])), particle2['radius'])

  # Desenhar as partículas
  pygame.draw.circle(window, BLUE, (int(particle1['x']), int(particle1['y'])), particle1['radius'])
  pygame.draw.circle(window, RED, (int(particle2['x']), int(particle2['y'])), particle2['radius'])

  # Atualizar os ângulos das partículas para a próxima iteração
  particle1['angle'] += particle1['speed']
  particle2['angle'] += particle2['speed']

  # Atualizar a janela
  pygame.display.flip()

# Loop principal do jogo
running = True
while running:
  # Limitar a taxa de quadros por segundo
  clock.tick(60)

  # Verificar eventos
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Desenhar as partículas
  draw()

# Encerrar o Pygame
pygame.quit()
