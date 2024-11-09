# cube.py
import random

import numpy as np

# Konstanta
MAGIC_CONST = 315  # Nilai konstanta magic untuk perhitungan objektif

# Membuat magic cube baru dengan angka unik dari 1 hingga 125
def create_magic_cube():
    """Membuat magic cube berukuran 5x5x5 dengan angka unik dari 1 sampai 125."""
    return random.sample(range(1, 126), 125)

# Fungsi untuk menghitung nilai objektif dari sebuah magic cube
def objective_function(magic_cube):
    """Menghitung nilai objektif dari magic cube berdasarkan jumlah baris, kolom, dan diagonal yang mencapai MAGIC_CONST."""
    point = 0
    for k in range(5):  # Setiap layer
        for j in range(5):
            line_sum_1 = line_sum_2 = line_sum_3 = 0
            for i in range(5):
                line_sum_1 += magic_cube[25 * k + 5 * j + i]       # Baris dalam satu layer
                line_sum_2 += magic_cube[25 * k + 5 * i + j]       # Kolom dalam satu layer
                line_sum_3 += magic_cube[25 * j + 5 * i + k]       # Diagonal pada layer
            if line_sum_1 == MAGIC_CONST: point += 1
            if line_sum_2 == MAGIC_CONST: point += 1
            if line_sum_3 == MAGIC_CONST: point += 1
            
            
        # diagonal wajah
    for j in range(5):
        # line_sum = [0] * 6 /////
        line_sum_1 = 0
        line_sum_2 = 0
        line_sum_3 = 0
        line_sum_4 = 0
        line_sum_5 = 0
        line_sum_6 = 0
        for i in range(5):
            mirr = 4 - i
            line_sum_1 += magic_cube[25 * j + 5 * i + i] # kiri atas ke kanan bawah (k)
            line_sum_2 += magic_cube[25 * j + 5 * i + mirr]  #kanan atas ke kiri bawah (k)
            line_sum_3 += magic_cube[25 * i + 5 * j + i] # kiri atas ke kanan bawah (i)
            line_sum_4 += magic_cube[25 * i + 5 * j + mirr] #kanan atas ke kiri bawah (i)     //nanti gw jelasin ini di kerkom kita ya gess
            line_sum_5 += magic_cube[25 * i + 5 * i + j]#kanan atas ke kiri bawah (j)
            line_sum_6 += magic_cube[25 * i + 5 * mirr + j] #kiri atas ke kanan bawah (j)
        # point += sum(1 for line_sum in line_sum if line_sum == MAGIC_CONST)  /////
        if line_sum_1 == MAGIC_CONST: point += 1
        if line_sum_2 == MAGIC_CONST: point += 1
        if line_sum_3 == MAGIC_CONST: point += 1
        if line_sum_4 == MAGIC_CONST: point += 1
        if line_sum_5 == MAGIC_CONST: point += 1
        if line_sum_6 == MAGIC_CONST: point += 1
            
            
    #diagonal ruang
    # line_sum = [0] * 4 //////
    line_sum_1 = 0
    line_sum_2 = 0
    line_sum_3 = 0
    line_sum_4 = 0
    for i in range(5):
        mirr = 4 - i
        line_sum_1 += magic_cube[25 * i + 5 * i + i] #intinya dari 25 ke 101 dah
        line_sum_2 += magic_cube[25 * i + 5 * i + mirr] # dari 90 ke 36
        line_sum_3 += magic_cube[25 * mirr + 5 * i + i] # dari pojok bawah ampe 5 pokonya mah
        line_sum_4 += magic_cube[25 * mirr + 5 * i + mirr] # dari 59 ke 67
    # point += sum(1 for line_sum in line_sum if line_sum == MAGIC_CONST) /////
    if line_sum_1 == MAGIC_CONST: point += 1
    if line_sum_2 == MAGIC_CONST: point += 1
    if line_sum_3 == MAGIC_CONST: point += 1
    if line_sum_4 == MAGIC_CONST: point += 1
    return float(point)


def initialize_cube(self):
    numbers = np.arange(1, self.N**3 + 1)
    np.random.shuffle(numbers)
    return numbers.reshape((self.N, self.N, self.N))
# Fungsi mutasi untuk magic cube, menukar posisi angka dalam magic cube
def mutate(cube, mutation_rate=0.05):
    """Mutasi magic cube dengan menukar beberapa angka secara acak, berdasarkan mutation_rate."""
    num_swaps = random.randint(1, 3)  # Tentukan berapa kali swap
    for _ in range(num_swaps):
        if random.random() < mutation_rate:
            i, j = random.sample(range(125), 2)
            cube[i], cube[j] = cube[j], cube[i]
            
#PUSINGGG            
def transform_to_3d(cube):
    """Mengubah list berukuran 125 menjadi 5x5x5 magic cube (3D array)."""
    return np.array(cube).reshape(5, 5, 5)

# Membuat magic cube
cube = create_magic_cube()

# Mengubahnya menjadi bentuk 5x5x5
magic_cube = transform_to_3d(cube)

# Menampilkan hasil
# print(magic_cube)
