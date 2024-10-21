import numpy as np


def random_restart_hill_climbing(magic_number, max_restart=10):
    best_cube = None
    best_score = float('inf')
    
    for _ in range(max_restart):
        cube = np.random.permutation(np.arange(1, 126)).reshape(5, 5, 5)  # Restart dengan kondisi acak
        final_cube, final_score = steepest_ascent_hill_climbing(cube, magic_number)
        
        if final_score < best_score:
            best_cube, best_score = final_cube, final_score
    
    return best_cube, best_score
cube = np.random.permutation(np.arange(1, 126)).reshape(5, 5, 5)  # Kubus 5x5x5
magic_number = 315  # Contoh magic number
initial_cube, final_cube, final_score, scores, iterations, duration = steepest_ascent_hill_climbing(cube, magic_number)