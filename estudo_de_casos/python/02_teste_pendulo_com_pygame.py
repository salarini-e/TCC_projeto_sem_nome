import pygame
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

# Inicialização do Pygame
pygame.init()

# Configurações da janela
width = 1100
height = 700
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Animação de Pêndulo')

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Parâmetros do pêndulo
pendulum_length = 200
gravity = 9.8
initial_angle = -2*math.pi / 4
angle = initial_angle
angular_velocity = 0.0

# Configurações do gráfico
fig = plt.Figure(figsize=(6, 4), dpi=100)
canvas = FigureCanvas(fig)
ax = fig.add_subplot(111)
time_data = []
angle_data = []
line, = ax.plot(time_data, angle_data, 'b-')
ax.set_xlim(0, 10)
ax.set_ylim(-math.pi, math.pi)
ax.set_xlabel('Tempo (s)')
ax.set_ylabel('Ângulo (rad)')
ax.set_title('Gráfico do Pêndulo')

# Posição do pêndulo
pendulum_x = width // 4
pendulum_y = height // 2

# Configurações do texto
font = pygame.font.Font(None, 24)

# Botão "Start/Pause"
button_text = font.render('Start', True, BLACK)
button_rect = button_text.get_rect()
button_rect.bottomright = (width - 10, height - 10)
button_clicked = False

# Limite do gráfico
graph_time_limit = 10
graph_data_limit = 500
graph_x_start = 0

# Margem da animação em relação à borda
animation_margin = 80

# Loop principal
running = True
clock = pygame.time.Clock()

while running:
    # Limitar a taxa de quadros
    clock.tick(60)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                button_clicked = not button_clicked

    # Atualizar o ângulo e a velocidade angular se o botão foi clicado
    if button_clicked:
        angular_acceleration = -gravity / pendulum_length * math.sin(angle)
        angular_velocity += angular_acceleration
        angle += angular_velocity

    # Limpar a janela
    window.fill(WHITE)

    # Desenhar o pêndulo
    bob_x = pendulum_x + pendulum_length * math.sin(angle)
    bob_y = pendulum_y + pendulum_length * math.cos(angle)
    pygame.draw.line(window, BLACK, (pendulum_x, pendulum_y), (bob_x, bob_y), 2)
    pygame.draw.circle(window, BLACK, (bob_x, bob_y), 20)

    # Exibir a posição do círculo
    position_text = font.render(f'Posição: ({bob_x:.2f}, {bob_y:.2f})', True, BLACK)
    window.blit(position_text, (10, 10))

    # Exibir a velocidade angular do pêndulo
    angular_velocity_text = font.render(f'Velocidade Angular: {angular_velocity:.2f}', True, BLACK)
    window.blit(angular_velocity_text, (10, 40))

    # Atualizar o gráfico
    time_data.append(pygame.time.get_ticks() / 1000)
    angle_data.append(angle)

    if len(time_data) > graph_data_limit:
        time_data.pop(0)
        angle_data.pop(0)

    if time_data[-1] > graph_time_limit:
        ax.set_xlim(time_data[-1] - graph_time_limit, time_data[-1])

    line.set_data(time_data, angle_data)
    ax.relim()
    ax.autoscale_view()

    # Renderizar o gráfico
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_rgb()
    graph_surface = pygame.image.fromstring(raw_data, canvas.get_width_height(), 'RGB')

    # Exibir o gráfico
    graph_rect = graph_surface.get_rect()
    graph_rect.topright = (width - 10, animation_margin)
    window.blit(graph_surface, graph_rect)

    # Renderizar o botão "Start/Pause"
    pygame.draw.rect(window, RED, button_rect)
    button_text = font.render('Pause' if button_clicked else 'Start', True, WHITE)
    button_text_rect = button_text.get_rect()
    button_text_rect.center = button_rect.center
    window.blit(button_text, button_text_rect)

    # Atualizar a janela
    pygame.display.flip()

# Encerrar o Pygame
pygame.quit()
