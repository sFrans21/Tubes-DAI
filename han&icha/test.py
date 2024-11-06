import numpy as np

magic_cube = [
    [
        [25, 16, 80, 104, 90],
        [115, 98, 4, 1, 97],
        [42, 111, 52, 25, 75],
        [67, 18, 27, 102, 85],
        [87, 73, 106, 5, 44]
    ],
    [
        [91, 77, 71, 6, 70],
        [52, 64, 117, 61, 121],
        [30, 118, 21, 123, 23],
        [26, 32, 94, 44, 113],
        [116, 31, 14, 73, 81]
    ],
    [
        [47, 61, 45, 76, 86],
        [107, 43, 68, 86, 34],
        [83, 63, 88, 35, 94],
        [92, 93, 68, 63, 89],
        [40, 50, 82, 55, 88]
    ],
    [
        [31, 53, 112, 80, 55],
        [13, 82, 34, 87, 100],
        [51, 71, 47, 23, 93],
        [113, 57, 64, 57, 74],
        [40, 58, 112, 27, 61]
    ],
    [
        [121, 108, 70, 8, 37],
        [29, 28, 122, 125, 11],
        [103, 84, 94, 123, 60],
        [78, 54, 83, 62, 55],
        [36, 110, 42, 101, 21]
    ]
]


def generate_random_magic_cube(n):
    # Pastikan n adalah 5 untuk magic cube 5x5x5
    if n != 5:
        raise ValueError("Hanya mendukung magic cube 5x5x5.")
    
    # Buat array kosong untuk magic cube
    cube = np.zeros((n, n, n), dtype=int)
    
    # Buat list angka dari 1 hingga 125
    numbers = np.random.permutation(np.arange(1, n**3 + 1))
    
    # Mengisi cube dengan angka acak
    index = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                cube[i][j][k] = numbers[index]
                index += 1

    return cube

# Menghasilkan dan mencetak magic cube acak 5x5x5

magic_cube = generate_random_magic_cube(5)
print("Magic Cube 5x5x5:\n", magic_cube)


def objective_function(cube):
    target_sum = 315
    error = 0
    
    # Cek baris, kolom, dan lapisan
    for i in range(5):
        error += abs(np.sum(cube[i, :, :]) - target_sum)  # Baris pada sumbu x
        error += abs(np.sum(cube[:, i, :]) - target_sum)  # Kolom pada sumbu y
        error += abs(np.sum(cube[:, :, i]) - target_sum)  # Lapisan pada sumbu z

    # Cek diagonal
    error += abs(np.sum([cube[i, i, i] for i in range(5)]) - target_sum)
    error += abs(np.sum([cube[i, i, 4 - i] for i in range(5)]) - target_sum)
    error += abs(np.sum([cube[i, 4 - i, i] for i in range(5)]) - target_sum)
    error += abs(np.sum([cube[4 - i, i, i] for i in range(5)]) - target_sum)

    return error

def simulated_annealing(initial_cube, initial_temp, cooling_rate, max_iterations):
    current_cube = initial_cube.copy()
    current_error = objective_function(current_cube)
    
    best_cube = current_cube.copy()
    best_error = current_error
    
    temperature = initial_temp
    
    for iteration in range(max_iterations):
        # Menghasilkan dua indeks yang valid untuk swap
        x1 = np.random.randint(0, 5, size=3)  # Indeks untuk elemen pertama
        x2 = np.random.randint(0, 5, size=3)  # Indeks untuk elemen kedua

         # Ambil nilai dari current_cube di kedua indeks
        value1 = current_cube[tuple(x1)]
        value2 = current_cube[tuple(x2)]

         # Print kedua nilai yang akan ditukar
        print(f"Nilai yang akan ditukar: {value1} (indeks {x1}) dan {value2} (indeks {x2})")
        
        new_cube = current_cube.copy()
        # Melakukan swap antara dua elemen di posisi yang dipilih
        new_cube[tuple(x1)], new_cube[tuple(x2)] = new_cube[tuple(x2)], new_cube[tuple(x1)]
        
        new_error = objective_function(new_cube)
        
        # Terima solusi baru berdasarkan kriteria
        if new_error < current_error or np.random.rand() < np.exp((current_error - new_error) / temperature):
            current_cube = new_cube
            current_error = new_error
            
            # Simpan solusi terbaik
            if current_error < best_error:
                best_cube = current_cube.copy()
                best_error = current_error
        
        # Turunkan suhu
        temperature *= cooling_rate
    
    return best_cube, best_error


# Inisialisasi dan jalankan algoritma
initial_cube = generate_random_magic_cube(5)
best_cube, best_error = simulated_annealing(initial_cube, initial_temp=1000, cooling_rate=0.95, max_iterations=10000)

print("Best Magic Cube:\n", best_cube)
print("Best Error:", best_error)