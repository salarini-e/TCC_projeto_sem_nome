##DEU CERTOOOOO!

import pygame
import numpy as np
from scipy.spatial import cKDTree

# Configurações da simulação
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
ATOM_RADIUS = 4
RESTORATION_FORCE = 0.05  # Força de restauração dos átomos à sua posição inicial
MOUSE_FORCE = 2  # Força de afastamento em relação ao mouse
REPULSION_FORCE = 0.05  # Força de repulsão quando os átomos colidem
ATOM_COUNT = 50

# Inicialização do Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

def distribute_atoms_uniformly(num_atoms):
    step_x = SCREEN_WIDTH // (num_atoms // 2 + 1)
    step_y = SCREEN_HEIGHT // (num_atoms // 2 + 1)

    atoms = []
    for y in range(step_y, SCREEN_HEIGHT - step_y, step_y):
        for x in range(step_x, SCREEN_WIDTH - step_x, step_x):
            atoms.append((x, y))

    return np.array(atoms, dtype=np.float64)

# Criando átomos posicionados uniformemente na tela
atoms = distribute_atoms_uniformly(ATOM_COUNT)

# Posições iniciais dos átomos
atom_initial_positions = atoms.copy()

def calculate_forces(atoms, mouse_pos):
    forces = np.zeros_like(atoms)

    # Força de restauração dos átomos à sua posição inicial
    forces += (atom_initial_positions - atoms) * RESTORATION_FORCE

    # Força de afastamento em relação ao mouse
    dist_to_mouse = np.linalg.norm(atoms - mouse_pos, axis=1)
    forces += (atoms - mouse_pos) * MOUSE_FORCE / np.maximum(dist_to_mouse, 1.0)[:, np.newaxis]

    return forces

def update_positions(atoms, forces):
    # Atualizar as posições dos átomos com base nas forças aplicadas
    new_atoms = atoms + forces

    # Criar uma estrutura de grade para otimizar a detecção de colisões
    grid = cKDTree(new_atoms)

    # Verificar colisões entre os átomos e aplicar força de repulsão
    for i in range(len(new_atoms)):
        atom_pos = new_atoms[i]
        nearby_atoms_indices = grid.query_ball_point(atom_pos, 2 * ATOM_RADIUS)
        nearby_atoms_indices.remove(i)  # Remover o próprio átomo da lista de átomos próximos

        for j in nearby_atoms_indices:
            dist = np.linalg.norm(new_atoms[i] - new_atoms[j])
            if dist < 2 * ATOM_RADIUS:  # Os átomos colidiram
                repulsion_distance = 2 * ATOM_RADIUS
                repulsion_dir = (new_atoms[i] - new_atoms[j]) / dist
                repulsion_amount = (2 * ATOM_RADIUS - dist) / 2.0
                new_atoms[i] += repulsion_amount * repulsion_dir
                new_atoms[j] -= repulsion_amount * repulsion_dir

    # Manter os átomos dentro dos limites da tela
    new_atoms = np.clip(new_atoms, [ATOM_RADIUS, ATOM_RADIUS], [SCREEN_WIDTH - ATOM_RADIUS, SCREEN_HEIGHT - ATOM_RADIUS])

    return new_atoms

def main():
    global atoms

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Calcular as forças de interação e afastamento
        mouse_pos = np.array(pygame.mouse.get_pos(), dtype=np.float64)
        forces = calculate_forces(atoms, mouse_pos)

        # Atualizar as posições dos átomos
        atoms = update_positions(atoms, forces)

        # Renderização
        screen.fill((255, 255, 255))
        for atom in atoms:
            pygame.draw.circle(screen, (0, 0, 255), atom.astype(int), ATOM_RADIUS)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
