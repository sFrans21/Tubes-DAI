import numpy as np
import time
import matplotlib.pyplot as plt
def objective_function(cube, magic_number):
    # Hitung seberapa dekat jumlah setiap baris, kolom, tiang, dan diagonal dengan magic number
    score = 0
    # Implementasikan perhitungan fungsi objektif sesuai aturan Diagonal Magic Cube
    return score


def swap_positions(cube):
    # Flatten kubus menjadi array 1D
    flat_cube = cube.flatten()

    # Pilih dua indeks acak dalam array 1D
    i, j = np.random.randint(0, flat_cube.size, size=2)

    # Tukar posisi dua elemen di array 1D
    flat_cube[i], flat_cube[j] = flat_cube[j], flat_cube[i]

    # Kembalikan array 1D ke bentuk 3D (5x5x5)
    return flat_cube.reshape(5, 5, 5)

def steepest_ascent_hill_climbing(cube, magic_number):
    current_cube = cube.copy()
    current_score = objective_function(current_cube, magic_number)
    
    # Catat state awal
    initial_cube = current_cube.copy()
    
    # Catat nilai objective function di setiap iterasi
    scores = [current_score]  # Simpan nilai fungsi objektif dari state awal
    
    # Mulai stopwatch untuk menghitung durasi pencarian
    start_time = time.time()
    iterations = 0

    while True:
        next_cube = swap_positions(current_cube.copy())
        next_score = objective_function(next_cube, magic_number)
        
        if next_score < current_score:
            current_cube = next_cube
            current_score = next_score
        else:
            break  # Berhenti jika tidak ada perbaikan lebih lanjut
        iterations += 1
        
    # Catat state akhir
    final_cube = current_cube.copy()
    
    # Hitung durasi proses pencarian
    end_time = time.time()
    duration = end_time - start_time
    
    return initial_cube, final_cube, current_score, scores, iterations, duration

# Fungsi untuk menampilkan hasil dan plot
def plot_results(scores):
    plt.plot(range(len(scores)), scores)
    plt.title('Nilai Objective Function terhadap Iterasi')
    plt.xlabel('Iterasi')
    plt.ylabel('Nilai Objective Function')
    plt.show()
    
def random_restart_hill_climbing(magic_number, max_restart=10):
    best_cube = None
    best_score = float('inf')
    
    for _ in range(max_restart):
        cube = np.random.permutation(np.arange(1, 126)).reshape(5, 5, 5)  # Restart dengan kondisi acak
        final_cube, final_score = steepest_ascent_hill_climbing(cube, magic_number)
        
        if final_score < best_score:
            best_cube, best_score = final_cube, final_score
    
    return best_cube, best_score
# Contoh penggunaan
cube = np.random.permutation(np.arange(1, 126)).reshape(5, 5, 5)  # Kubus 5x5x5
magic_number = 30  # Contoh magic number
random_restart_hill_climbing(cube, magic_number)


# Cetak hasil
print("State Awal Kubus:\n", initial_cube)
print("State Akhir Kubus:\n", final_cube)
print("Nilai Objective Function Akhir:", final_score)
print("Jumlah Iterasi yang Dilewati:", iterations)
print("Durasi Proses Pencarian: {:.4f} detik".format(duration))

# Tampilkan plot nilai objective function
plot_results(scores)