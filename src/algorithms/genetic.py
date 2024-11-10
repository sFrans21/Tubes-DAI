import random
import matplotlib.pyplot as plt
import numpy as py
from gencube import create_magic_cube, objective_function, mutate, transform_to_3d
import time

# Konstanta
# POPULATION_SIZE = 1000     
TARGET_OBJECTIVE = 0  # Nilai sempurna

def select_parent(population):
    candidates = random.sample(population, 20)
    candidates.sort(key=lambda cube: abs(objective_function(cube) - TARGET_OBJECTIVE))
    return candidates[0]


# Fungsi crossover buat ngasilin anak dari dua parent
def crossover(parent1, parent2):
    size = len(parent1)
    child1, child2 = [None]*size, [None]*size
    start, end = sorted(random.sample(range(size), 2))
    
    # copy segment dari parent1 ke child1, terus parent2 ke child2
    child1[start:end+1] = parent1[start:end+1]
    child2[start:end+1] = parent2[start:end+1]
    
    # ngisi posisi yang masih kosong di child1 dari parent2 and vice versa tanpa ada duplikat
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
    iterations = int(input("Berikan jumlah iterasi/generasi: "))
    populations = int(input("Berikan jumlah populasi yang diinginkan: "))
    
    start_time = time.time()
    population = [create_magic_cube() for _ in range(populations)]
    best_cube = None
    best_objective_value = float('inf')
    objective_value_reg = []
    # iterations = 0
    
    
    time.sleep(1)
    print()
    print("State awal:")
    rand_pop = random.sample(population,1)  # ngambil satu state secara acak dari population sebagai state awal
    print(transform_to_3d(rand_pop))
    
    if (iterations <= 0):
        print("jumlah iterasi tidak boleh 0 atau kurang! jalankan ulang program")
    else:
        print("mengonfigurasi kubus.....")
        time.sleep(2)
    
    # Iterasi untuk nemuin solusi optimal
        for generation in range(iterations):  
            print(f"Generasi: {generation+1}")
            
            new_population = []
            
            while len(new_population) < populations:
                # Memilih dua parent terbaik
                parent1 = select_parent(population)
                parent2 = select_parent(population)
                
                # ngelakuin crossover untuk menghasilkan dua anak
                child1, child2 = crossover(parent1, parent2)
                
                # neglakuin mutasi pada anak
                mutate(child1)
                mutate(child2)
                
                # nambahin anak ke populasi baru
                new_population.append(child1)
                new_population.append(child2)
                
            
            
            # Populasi lama digantikan oleh populasi baru
            population = new_population
            
            # nentuin kubus terbaik dalam populasi baru
            current_best = min(population, key=lambda cube: abs(objective_function(cube) - TARGET_OBJECTIVE))
            current_best_value = objective_function(current_best)
            
            # meriksa apakah solusi saat ini lebih baik
            if abs(current_best_value - TARGET_OBJECTIVE) < abs(best_objective_value - TARGET_OBJECTIVE):
                best_cube = current_best
                best_objective_value = current_best_value
                
            objective_value_reg.append(best_objective_value)
            print(f"Nilai objektif terbaik saat ini: {best_objective_value}")
            print()
            
            # berhenti jika menemukan solusi optimal  (most likely gaakan kejadian but gaada salahnya)
            if best_objective_value == TARGET_OBJECTIVE:
                print("Solusi optimal ditemukan!")
                break
        
        end_time = time.time()
        duration = end_time - start_time
        
        # Menampilkan solusi terbaik
       
        print("Selesai!")
        time.sleep(1)
        print(f"Durasi pencarian: {duration:.2f} detik")
        print("\nState Kubus terbaik:")
        print(transform_to_3d(best_cube))
        time.sleep(2)
        print()

        
        
        # Visualisasi regresi
        plt.plot(objective_value_reg, marker='o')
        plt.title("Objective Function Progression")
        plt.xlabel("Generation")
        plt.ylabel("Best Objective Function")
        plt.show()


#runn
if __name__ == "__main__":
    genetic_algorithm()



