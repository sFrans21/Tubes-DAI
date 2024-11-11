# File: Magiccube.py
import numpy as np
from itertools import product

# Kubus akan di generate dari lapisan bawah ke lapisan atas. Jadi bayangkan saja layer1 ditumpuk layer2 ditumpuk layer3 dan seterusnya
class MagicCube:
    # Membuat kubus dengan ukuran N x N x N dan angka yang diacak
    def __init__(self, N=5, magic_number=315):
        self.N = N
        self.MAGIC_NUMBER = magic_number
        self.cube = self.initialize_cube()
    
    # Menginisialisasi kubus dengan angka yang diacak
    def initialize_cube(self):
        numbers = np.arange(1, self.N**3 + 1)
        np.random.shuffle(numbers)
        return numbers.reshape((self.N, self.N, self.N))
    
    # Menghitung skor objektif function dari kubus
    def fitness(self, cube=None):
        if cube is None:
            cube = self.cube

        cube = np.array(cube)

        if cube.shape != (self.N, self.N, self.N):
            raise ValueError(f"Ukuran kubus adalah {cube.shape}, seharusnya {(self.N, self.N, self.N)}")

        # Menghitung skor dari setiap baris, kolom, dan diagonal
        score = 0
        
        # Menghitung skor dari diagonal kubus
        score += abs(np.sum([cube[i, i, i] for i in range(self.N)]) - self.MAGIC_NUMBER)
        score += abs(np.sum([cube[i, i, self.N - i - 1] for i in range(self.N)]) - self.MAGIC_NUMBER)

        target = self.MAGIC_NUMBER * self.N
        for i in range(self.N):
            # Menghitung skor dari diagonal 
            score += abs(np.sum(np.diagonal(cube[i, :, :])) - self.MAGIC_NUMBER)
            score += abs(np.sum(np.diagonal(np.fliplr(cube[i, :, :]))) - self.MAGIC_NUMBER)
            score += abs(np.sum(np.diagonal(cube[:, i, :])) - self.MAGIC_NUMBER)
            score += abs(np.sum(np.diagonal(np.fliplr(cube[:, i, :]))) - self.MAGIC_NUMBER)
            score += abs(np.sum(np.diagonal(cube[:, :, i])) - self.MAGIC_NUMBER)
            score += abs(np.sum(np.diagonal(np.fliplr(cube[:, :, i]))) - self.MAGIC_NUMBER)

            score += abs(np.sum(cube[i, :, :]) - target)
            score += abs(np.sum(cube[:, i, :]) - target)
            score += abs(np.sum(cube[:, :, i]) - target)

        return score

    # Mencari tetangga dari kubus
    def neighbors_function(self, cube=None):
        if cube is None:
            cube = self.cube

        neighbors = []
        # Mencari semua kemungkinan posisi yang bisa ditukar
        positions = np.array(list(product(range(self.N), repeat=3)))

        for x, y, z in positions:
            for dx, dy, dz in product([-1, 0, 1], repeat=3):
                if dx == 0 and dy == 0 and dz == 0:
                    continue
                nx, ny, nz = x + dx, y + dy, z + dz
                if 0 <= nx < self.N and 0 <= ny < self.N and 0 <= nz < self.N:
                    swap_cube = cube.copy()
                    swap_cube[x, y, z], swap_cube[nx, ny, nz] = swap_cube[nx, ny, nz], swap_cube[x, y, z]
                    neighbors.append(swap_cube)

        return neighbors