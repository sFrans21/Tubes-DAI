import random
import matplotlib.pyplot as plt
import numpy as py
from cube import create_magic_cube, objective_function, mutate

# Konstanta
POPULATION_SIZE = 1000
TARGET_OBJECTIVE = 109  # Nilai target untuk nilai objektif

# Fungsi seleksi untuk memilih parent terbaik dari populasi secara acak
def select_parent(population):
    """Memilih satu parent terbaik dari 20 kandidat yang dipilih secara acak."""
    candidates = random.sample(population, 20)
    candidates.sort(key=lambda cube: abs(objective_function(cube) - TARGET_OBJECTIVE))
    return candidates[0]

# Fungsi crossover untuk menghasilkan anak dari dua parent
def crossover(parent1, parent2):
    """Menghasilkan dua anak dengan crossover dari dua parent menggunakan order crossover."""
    size = len(parent1)
    child1, child2 = [None]*size, [None]*size
    start, end = sorted(random.sample(range(size), 2))
    
    # Copy segment from parent1 to child1 and parent2 to child2
    child1[start:end+1] = parent1[start:end+1]
    child2[start:end+1] = parent2[start:end+1]
    
    # Fill the remaining positions in child1 from parent2 and vice versa without duplicating
    fill_remaining(child1, parent2, start, end)
    fill_remaining(child2, parent1, start, end)
    
    return child1, child2

def fill_remaining(child, parent, start, end):
    """Fills remaining positions in child array."""
    size = len(parent)
    child_pos = end + 1
    parent_pos = end + 1
    while None in child:
        if parent[parent_pos % size] not in child:
            child[child_pos % size] = parent[parent_pos % size]
            child_pos += 1
        parent_pos += 1


# Algoritma Genetika
def genetic_algorithm():
    """Menjalankan algoritma genetika untuk menemukan magic cube terbaik."""
    # Membuat populasi awal
    population = [create_magic_cube() for _ in range(POPULATION_SIZE)]
    best_cube = None
    best_objective_value = float('inf')
    
    # Iterasi untuk menemukan solusi optimal
    for generation in range(15):  # Maksimum 100 generasi
        print(f"Generasi: {generation+1}")
        
        new_population = []
        
        while len(new_population) < POPULATION_SIZE:
            # Memilih dua parent terbaik
            parent1 = select_parent(population)
            parent2 = select_parent(population)
            
            # Melakukan crossover untuk menghasilkan dua anak
            child1, child2 = crossover(parent1, parent2)
            
            # Melakukan mutasi pada anak
            mutate(child1)
            mutate(child2)
            
            # Menambahkan anak ke populasi baru
            new_population.append(child1)
            new_population.append(child2)
        
        # Populasi lama digantikan oleh populasi baru
        population = new_population
        
        # Menentukan kubus terbaik dalam populasi baru
        current_best = min(population, key=lambda cube: abs(objective_function(cube) - TARGET_OBJECTIVE))
        current_best_value = objective_function(current_best)
        
        # Memeriksa apakah solusi saat ini lebih baik
        if abs(current_best_value - TARGET_OBJECTIVE) < abs(best_objective_value - TARGET_OBJECTIVE):
            best_cube = current_best
            best_objective_value = current_best_value
        
        print(f"Nilai objektif terbaik saat ini: {best_objective_value}")
        
        # Hentikan jika menemukan solusi optimal
        if best_objective_value == TARGET_OBJECTIVE:
            print("Solusi optimal ditemukan!")
            break

    # Menampilkan solusi terbaik
    print("\nKubus terbaik:")
    print(best_cube)
    print("Nilai objektif terbaik:", best_objective_value)

# Menjalankan algoritma genetika
if __name__ == "__main__":
    genetic_algorithm()
