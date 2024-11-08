# Cara penggunaan, saat kode dijalankan, akan muncul visualisasi kubus awal
# Silang pop up tersebut maka algoritma akan berjalan
# Setelah menunggu beberapa detik, akan muncul visualisasi kubus akhir

import numpy as np
import matplotlib.pyplot as plt
import time
from itertools import product

# Visualisasi setiap lapisan dari kubus dalam tabel angka
def plot_cube(cube, title):
    fig, axes = plt.subplots(1, cube.shape[0], figsize=(15, 5))
    fig.suptitle(title, fontsize=16)
    
    for i in range(cube.shape[0]):
        ax = axes[i]
        ax.matshow(np.zeros_like(cube[i]), cmap="Blues", alpha=0.1)  # Kotak kosong untuk menampilkan angka
        for (j, k), val in np.ndenumerate(cube[i]):
            ax.text(k, j, str(val), ha='center', va='center', fontsize=8)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title(f"Layer {i + 1}")
    plt.show()

# Steepest Hill Climbing Algorithm
class SteepestHillClimbing:
    def __init__(self, max_iterations=1000):
        self.solver = MagicCube()
        self.initial_state = self.solver.cube
        self.objective_function = self.solver.fitness(self.initial_state)
        self.max_iterations = max_iterations

    def search(self):
        iteration_count = 1
        start_time = time.time()

        while iteration_count <= self.max_iterations:
            neighbors = self.solver.neighbors_function(self.initial_state)
            best_neighbor = None
            best_score = self.objective_function            
            
            for neighbor in neighbors:
                neighbor_score = self.solver.fitness(neighbor)
                if neighbor_score < best_score:
                    best_score = neighbor_score
                    best_neighbor = neighbor

            if best_neighbor is None:
                break

            self.initial_state = best_neighbor
            self.objective_function = best_score
            
            if self.is_solved(self.objective_function):
                break
            
            iteration_count += 1

        end_time = time.time()
        execution_time = end_time - start_time
        return self.initial_state, self.objective_function, execution_time

    def is_solved(self, score):
        return score == 0

# Magic Cube Class
class MagicCube:
    def __init__(self, N=5, magic_number=315):
        self.N = N
        self.MAGIC_NUMBER = magic_number
        self.cube = self.initialize_cube()
    
    def initialize_cube(self):
        numbers = np.arange(1, self.N**3 + 1)
        np.random.shuffle(numbers)
        return numbers.reshape((self.N, self.N, self.N))
    
    # Menghitung skor heuristik dari kubus
    def fitness(self, cube=None):
        if cube is None:
            cube = self.cube

        cube = np.array(cube)
        score = 0
        for i in range(self.N):
            score += abs(np.sum(cube[i, :, :]) - self.MAGIC_NUMBER * self.N)
            score += abs(np.sum(cube[:, i, :]) - self.MAGIC_NUMBER * self.N)
            score += abs(np.sum(cube[:, :, i]) - self.MAGIC_NUMBER * self.N)
            score += abs(np.sum(np.diagonal(cube[i, :, :])) - self.MAGIC_NUMBER)
            score += abs(np.sum(np.diagonal(np.fliplr(cube[i, :, :]))) - self.MAGIC_NUMBER)
            score += abs(np.sum(np.diagonal(cube[:, i, :])) - self.MAGIC_NUMBER)
            score += abs(np.sum(np.diagonal(np.fliplr(cube[:, i, :]))) - self.MAGIC_NUMBER)
            score += abs(np.sum(np.diagonal(cube[:, :, i])) - self.MAGIC_NUMBER)
            score += abs(np.sum(np.diagonal(np.fliplr(cube[:, :, i]))) - self.MAGIC_NUMBER)

        score += abs(np.sum([cube[i, i, i] for i in range(self.N)]) - self.MAGIC_NUMBER)
        score += abs(np.sum([cube[i, i, self.N - i - 1] for i in range(self.N)]) - self.MAGIC_NUMBER)

        return score

    # Generate neighbors by swapping adjacent elements
    def neighbors_function(self, cube=None):
        if cube is None:
            cube = self.cube

        neighbors = []
        positions = np.array(list(product(range(self.N), repeat=3)))

        for x, y, z in positions:
            for dx, dy, dz in product([-1, 0, 1], repeat=3):
                if dx == 0 and dy == 0 and dz == 0:
                    continue
                nx, ny, nz = x + dx, y + dy, z + dz
                if 0 <= nx < self.N and 0 <= ny < self.N and 0 <= nz < self.N:
                    new_cube = cube.copy()
                    new_cube[x, y, z], new_cube[nx, ny, nz] = new_cube[nx, ny, nz], new_cube[x, y, z]
                    neighbors.append(new_cube)

        return neighbors

# Main program
main = SteepestHillClimbing(max_iterations=100)
initial_state = main.initial_state
initial_score = main.objective_function

# Visualisasi kondisi awal
plot_cube(initial_state, f"Initial State of the Cube (Score: {initial_score})")

# Menjalankan pencarian lokal
final_state, final_score, execution_time = main.search()

# Visualisasi kondisi akhir
plot_cube(final_state, f"Final State of the Cube (Score: {final_score}, Time: {execution_time:.2f} seconds)")
