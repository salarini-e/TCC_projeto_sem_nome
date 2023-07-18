import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parâmetros do pêndulo
length = 1.0
gravity = 9.8
initial_angle = np.pi / 4

# Criação da figura e dos eixos
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.set_xlim(-length - 0.2, length + 0.2)
ax1.set_ylim(-length - 0.2, length + 0.2)
ax1.set_aspect('equal')
ax1.grid(True)

# Inicialização das linhas do pêndulo
pendulum_line, = ax1.plot([], [], 'o-', lw=2)

# Inicialização das linhas do gráfico
time_data = []
angle_data = []
graph_line, = ax2.plot([], [], lw=2)

# Função de inicialização da animação
def init():
    pendulum_line.set_data([], [])
    graph_line.set_data([], [])
    return pendulum_line, graph_line

# Função de atualização da animação
def update(frame):
    time = frame / 100.0  # Fator de escala para o tempo
    angle = initial_angle * np.cos(np.sqrt(gravity/length) * time)
    x = length * np.sin(angle)
    y = -length * np.cos(angle)

    # Atualização das linhas do pêndulo
    pendulum_line.set_data([0, x], [0, y])

    # Atualização dos dados do gráfico
    time_data.append(time)
    angle_data.append(angle)
    graph_line.set_data(time_data, angle_data)

    return pendulum_line, graph_line

# Criação da animação
animation = FuncAnimation(fig, update, frames=range(100), init_func=init, blit=True)

# Exibição da animação
plt.show()
