import pygame
import sys

# Inicializar o Pygame
pygame.init()

# Configurações da janela
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Simulação de Partículas")

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Variáveis para armazenar os dados das partículas
particle1 = {
    'mass': None,
    'position': None,
    'velocity': None
}

particle2 = {
    'mass': None,
    'position': None,
    'velocity': None
}

# Função para exibir texto na tela
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    window.blit(text_surface, text_rect)

# Função para obter o valor de uma caixa de entrada de texto
def get_input_box_value(rect, font):
    input_box = pygame.Rect(rect)
    color_inactive = BLACK
    color_active = BLACK
    color = color_inactive
    active = False
    text = ""

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return text
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        window.fill(WHITE)
        pygame.draw.rect(window, color, input_box, 2)
        draw_text("Massa da Partícula 1:", font, BLACK, 50, 50)
        draw_text("Posição da Partícula 1:", font, BLACK, 50, 100)
        draw_text("Velocidade da Partícula 1:", font, BLACK, 50, 150)

        draw_text("Massa da Partícula 2:", font, BLACK, 50, 250)
        draw_text("Posição da Partícula 2:", font, BLACK, 50, 300)
        draw_text("Velocidade da Partícula 2:", font, BLACK, 50, 350)

        draw_text("Pressione Enter para iniciar a simulação", font, BLACK, window_width // 2, 500)

        input_rect = pygame.Rect(250, 50, 140, 32)
        pygame.draw.rect(window, color, input_rect)
        draw_text(text, font, BLACK, input_rect.x + 5, input_rect.y + 5)

        pygame.display.flip()

# Loop principal do programa
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Obter os valores das caixas de entrada
                particle1['mass'] = get_input_box_value((250, 50, 140, 32), pygame.font.Font(None, 24))
                particle1['position'] = get_input_box_value((250, 100, 140, 32), pygame.font.Font(None, 24))
                particle1['velocity'] = get_input_box_value((250, 150, 140, 32), pygame.font.Font(None, 24))

                particle2['mass'] = get_input_box_value((250, 250, 140, 32), pygame.font.Font(None, 24))
                particle2['position'] = get_input_box_value((250, 300, 140, 32), pygame.font.Font(None, 24))
                particle2['velocity'] = get_input_box_value((250, 350, 140, 32), pygame.font.Font(None, 24))

                # print("Dados da Partícula 1:")
                # print("Massa:", particle1['mass'])
                # print("Posição:", particle1['position'])
                # print("Velocidade:", particle1['velocity'])
                # print()

                # print("Dados da Partícula 2:")
                # print("Massa:", particle2['mass'])
                # print("Posição:", particle2['position'])
                # print("Velocidade:", particle2['velocity'])
                # print()