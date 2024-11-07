import numpy as np
from itertools import product

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

        if cube.shape != (self.N, self.N, self.N):
            raise ValueError(f"Ukuran kubus adalah {cube.shape}, seharusnya {(self.N, self.N, self.N)}")

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
                # Pastikan operasi pertukaran dilakukan pada bentuk 3D
                new_cube[x, y, z], new_cube[nx, ny, nz] = new_cube[nx, ny, nz], new_cube[x, y, z]
                neighbors.append((new_cube, (x, y, z), new_cube[x, y, z], (nx, ny, nz), new_cube[nx, ny, nz]))

    return neighbors