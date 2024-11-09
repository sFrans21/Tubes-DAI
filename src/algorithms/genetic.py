# # genetic_algorithm.py
# import random
# from cube import create_magic_cube, objective_function, mutate

# # Konstanta
# POPULATION_SIZE = 1000
# TARGET_OBJECTIVE = 109  # Nilai target untuk nilai objektif

# # Fungsi seleksi untuk memilih parent terbaik dari populasi secara acak
# def select_parent(population):
#     """Memilih satu parent terbaik dari 20 kandidat yang dipilih secara acak."""
#     candidates = random.sample(population, 20)
#     candidates.sort(key=lambda cube: abs(objective_function(cube) - TARGET_OBJECTIVE))
#     return candidates[0]

# # Fungsi crossover untuk menghasilkan anak dari dua parent
# def crossover(parent1, parent2):
#     """Menghasilkan dua anak dengan crossover dari dua parent."""
#     crossover_point = random.randint(1, 124)
#     child1 = parent1[:crossover_point] + parent2[crossover_point:]
#     child2 = parent2[:crossover_point] + parent1[crossover_point:]
#     return child1, child2

# # Algoritma Genetika
# def genetic_algorithm():
#     """Menjalankan algoritma genetika untuk menemukan magic cube terbaik."""
#     # Membuat populasi awal
#     population = [create_magic_cube() for _ in range(POPULATION_SIZE)]
#     best_cube = None
#     best_objective_value = float('inf')
    
#     # Iterasi untuk menemukan solusi optimal
#     for generation in range(100):  # Maksimum 100 generasi
#         print(f"Generasi: {generation+1}")
        
#         new_population = []
        
#         while len(new_population) < POPULATION_SIZE:
#             # Memilih dua parent terbaik
#             parent1 = select_parent(population)
#             parent2 = select_parent(population)
            
#             # Melakukan crossover untuk menghasilkan dua anak
#             child1, child2 = crossover(parent1, parent2)
            
#             # Melakukan mutasi pada anak
#             mutate(child1)
#             mutate(child2)
            
#             # Menambahkan anak ke populasi baru
#             new_population.append(child1)
#             new_population.append(child2)
        
#         # Populasi lama digantikan oleh populasi baru
#         population = new_population
        
#         # Menentukan kubus terbaik dalam populasi baru
#         current_best = min(population, key=lambda cube: abs(objective_function(cube) - TARGET_OBJECTIVE))
#         current_best_value = oimport logging


#         # Menentukan kubus terbaik dalam populasi baru
#         current_best = min(population, key=lambda cube: abs(objective_function(cube) - TARGET_OBJECTIVE))
#         current_best_value = objective_function(current_best)
        
#         # Memeriksa apakah solusi saat ini lebih baik
#         if abs(current_best_value - TARGET_OBJECTIVE) < abs(best_objective_value - TARGET_OBJECTIVE):
#             best_cube = current_best
#             best_objectivea genetika untuk menemukan magic cube terbaik."""
#     logging.info("Memulai algoritma genetika")
#     # Membuat
#     """Menjalankan algoritma genetika untuk menemukan magic cubever_point = random.randint(1, 124)
#     child1sover dari dua parent."""
#    objektif


# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# # Fungsi seleksi untukbjective_function(current_best)
        
#         # Memeriksa apakah solusi saat ini lebih baik
#         if abs(current_best_value - TARGET_OBJECTIVE) < abs(best_objective_value - TARGET_OBJECTIVE):
#             best_cube = current_best
#             best_objective_value = current_best_value
        
#         print(f"Nilai objektif terbaik saat ini: {best_objective_value}")
        
#         # Hentikan jika menemukan solusi optimal
#         if best_objective_value == TARGET_OBJECTIVE:
#             print("Solusi optimal ditemukan!")
#             break

#     # Menampilkan solusi terbaik
#     print("\nKubus terbaik:")
#     print(best_cube)
#     print("Nilai objektif terbaik:", best_objective_value)

# # Menjalankan algoritma genetika
# if __name__ == "__main__":
#     genetic_algorithm()




# genetic_algorithm.py
# import random
# from cube import create_magic_cube, objective_function, mutate

# # Konstanta
# POPULATION_SIZE = 1000
# TARGET_OBJECTIVE = 109  # Nilai target untuk nilai objektif

# # Fungsi seleksi untuk memilih parent terbaik dari populasi secara acak
# def select_parent(population):
#     """Memilih satu parent terbaik dari 20 kandidat yang dipilih secara acak."""
#     candidates = random.sample(population, 20)
#     candidates.sort(key=lambda cube: abs(objective_function(cube) - TARGET_OBJECTIVE))
#     return candidates[0]

# # Fungsi crossover untuk menghasilkan anak dari dua parent
# def crossover(parent1, parent2):
#     """Menghasilkan dua anak dengan crossover dari dua parent."""
#     crossover_point = random.randint(1, 124)
#     child1 = parent1[:crossover_point] + parent2[crossover_point:]
#     child2 = parent2[:crossover_point] + parent1[crossover_point:]
#     return child1, child2

# # Algoritma Genetika
# def genetic_algorithm():
#     """Menjalankan algoritma genetika untuk menemukan magic cube terbaik."""
#     # Membuat populasi awal
#     population = [create_magic_cube() for _ in range(POPULATION_SIZE)]
#     best_cube = None
#     best_objective_value = float('inf')
    
#     # Iterasi untuk menemukan solusi optimal
#     for generation in range(100):  # Maksimum 100 generasi
#         print(f"Generasi: {generation+1}")
        
#         new_population = []
        
#         while len(new_population) < POPULATION_SIZE:
#             # Memilih dua parent terbaik
#             parent1 = select_parent(population)
#             parent2 = select_parent(population)
            
#             # Melakukan crossover untuk menghasilkan dua anak
#             child1, child2 = crossover(parent1, parent2)
            
#             # Melakukan mutasi pada anak
#             mutate(child1)
#             mutate(child2)
            
#             # Menambahkan anak ke populasi baru
#             new_population.append(child1)
#             new_population.append(child2)
        
#         # Populasi lama digantikan oleh populasi baru
#         population = new_population
        
#         # Menentukan kubus terbaik dalam populasi baru
#         current_best = min(population, key=lambda cube: abs(objective_function(cube) - TARGET_OBJECTIVE))
#         current_best_value = objective_function(current_best)
        
#         # Memeriksa apakah solusi saat ini lebih baik
#         if abs(current_best_value - TARGET_OBJECTIVE) < abs(best_objective_value - TARGET_OBJECTIVE):
#             best_cube = current_best
#             best_objective_value = current_best_value
        
#         print(f"Nilai objektif terbaik saat ini: {best_objective_value}")
        
#         # Hentikan jika menemukan solusi optimal
#         if best_objective_value == TARGET_OBJECTIVE:
#             print("Solusi optimal ditemukan!")
#             break

#     # Menampilkan solusi terbaik
#     print("\nKubus terbaik:")
#     print(best_cube)
#     print("Nilai objektif terbaik:", best_objective_value)

# # Menjalankan algoritma genetika
# if __name__ == "__main__":
#     genetic_algorithm()



# INI YANG BARU
import random
import matplotlib.pyplot as plt
import numpy as py
from cube import create_magic_cube, objective_function, mutate, transform_to_3d
import time

# Konstanta
POPULATION_SIZE = 1000
TARGET_OBJECTIVE = 0  # Nilai target untuk nilai objektif

# Fungsi seleksi untuk memilih parent terbaik dari populasi secara acak
def select_parent(population):
    # Memilih satu parent terbaik dari 20 kandidat yang dipilih secara acak
    candidates = random.sample(population, 20)
    candidates.sort(key=lambda cube: abs(objective_function(cube) - TARGET_OBJECTIVE))
    return candidates[0]


# Fungsi crossover untuk menghasilkan anak dari dua parent
def crossover(parent1, parent2):
    # Menghasilkan dua anak dengan crossover dari dua parent
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

    time.sleep(1)
    population = [create_magic_cube() for _ in range(POPULATION_SIZE)]
    best_cube = None
    best_objective_value = float('inf')
    objective_value_reg = []
    iterations = 0
    
    iterations = int(input("Berikan jumlah iterasi/generasi: "))
    if (iterations <= 0):
        print("jumlah iterasi tidak boleh 0 atau kurang! jalankan ulang program")
    else:
        print("membuat populasi awal.....")
        time.sleep(1)
        print("mengonfigurasi kubus.....")
        time.sleep(1)
    # Iterasi untuk nemuin solusi optimal
        for generation in range(iterations):  # Maksimum 100 generasi
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
                
            objective_value_reg.append(best_objective_value)
            print(f"Nilai objektif terbaik saat ini: {best_objective_value}")
            print()
            
            # Hentikan jika menemukan solusi optimal
            if best_objective_value == TARGET_OBJECTIVE:
                print("Solusi optimal ditemukan!")
                break
        
        # Menampilkan solusi terbaik
        time.sleep(1)
        print("Selesai!")
        time.sleep(1)

        print("\nState Kubus terbaik:")
        print(transform_to_3d(best_cube))
        time.sleep(2)
        print()
        # print("Nilai objektif terbaik:", best_objective_value)
      #   perfection_percentage = round((best_objective_value/TARGET_OBJECTIVE * 100), 2)
      #   print(f'Persentase Kesempurnaaan: {perfection_percentage}%, ({best_objective_value}/{TARGET_OBJECTIVE})')
        
        
        # Visualisasi regresi
        plt.plot(objective_value_reg, marker='o')
        plt.title("Objective Value Progression")
        plt.xlabel("Generation")
        plt.ylabel("Best Objective Value")
        plt.show()

#runn
if __name__ == "__main__":
    genetic_algorithm()


