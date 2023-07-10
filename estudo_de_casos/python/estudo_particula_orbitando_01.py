import tkinter as tk
import math

# Configurar a janela
window = tk.Tk()
window.title("Partícula Orbitando em Canvas")
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# Definir as propriedades das partículas
particle1 = {
  'x': canvas.winfo_width() / 2,    # Posição X da partícula 1
  'y': canvas.winfo_height() / 2,   # Posição Y da partícula 1
  'radius': 20,                     # Raio da partícula 1
  'speed': 0.03,                    # Velocidade de rotação da partícula 1
  'angle': 0                        # Ângulo inicial da partícula 1
}

particle2 = {
  'x': canvas.winfo_width() / 2,    # Posição X da partícula 2
  'y': canvas.winfo_height() / 2,   # Posição Y da partícula 2
  'radius': 10,                     # Raio da partícula 2
  'speed': 0.1,                     # Velocidade de rotação da partícula 2
  'angle': 0                        # Ângulo inicial da partícula 2
}

def draw():
  # Limpar o canvas
  canvas.delete("all")

  # Calcular as novas posições das partículas
  particle1['x'] = canvas.winfo_width() / 2 + math.cos(particle1['angle']) * 100
  particle1['y'] = canvas.winfo_height() / 2 + math.sin(particle1['angle']) * 100

  particle2['x'] = particle1['x'] + math.cos(particle2['angle']) * 50
  particle2['y'] = particle1['y'] + math.sin(particle2['angle']) * 50

  # Desenhar as partículas
  canvas.create_oval(
    particle1['x'] - particle1['radius'],
    particle1['y'] - particle1['radius'],
    particle1['x'] + particle1['radius'],
    particle1['y'] + particle1['radius'],
    fill="blue"
  )

  canvas.create_oval(
    particle2['x'] - particle2['radius'],
    particle2['y'] - particle2['radius'],
    particle2['x'] + particle2['radius'],
    particle2['y'] + particle2['radius'],
    fill="red"
  )

  # Atualizar os ângulos das partículas para a próxima iteração
  particle1['angle'] += particle1['speed']
  particle2['angle'] += particle2['speed']

  # Repetir a animação
  canvas.after(10, draw)

# Iniciar a animação
draw()

# Executar o loop principal da janela
window.mainloop()
