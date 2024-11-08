import matplotlib.pyplot as plt
import numpy as np
from cube import create_magic_cube, objective_function, mutate
from genetic import genetic_algorithm, select_parent, crossover

# Fungsi untuk menampilkan kubus dalam format 3D (5 layer 5x5)
# def display_cube(cube, title="Cube State"):
#     cube_array = np.array(cube).reshape((5, 5, 5))
#     fig, axes = plt.subplots(1, 5, figsize=(15, 3))
#     fig.suptitle(title)
#     for i in range(5):
#         axes[i].imshow(cube_array[i], cmap="viridis", aspect='auto')
#         axes[i].set_title(f"Layer {i+1}")
#         axes[i].axis('off')
#     plt.show()

# Algoritma genetika dengan logging hasil eksperimen per generasi
def genetic_algorithm_with_visualization():
    POPULATION_SIZE = 1000
    TARGET_OBJECTIVE = 109
    population = [create_magic_cube() for _ in range(POPULATION_SIZE)]
    best_cube = None
    best_objective_value = float('inf')
    objective_values = []

    # Menyimpan state awal
#     display_cube(population[0], title="Initial Cube State")

    for generation in range(15):
        new_population = []
        while len(new_population) < POPULATION_SIZE:
            parent1 = select_parent(population)
            parent2 = select_parent(population)
            child1, child2 = crossover(parent1, parent2)
            mutate(child1)
            mutate(child2)
            new_population.append(child1)
            new_population.append(child2)

        population = new_population
        current_best = min(population, key=lambda cube: abs(objective_function(cube) - TARGET_OBJECTIVE))
        current_best_value = objective_function(current_best)

        if abs(current_best_value - TARGET_OBJECTIVE) < abs(best_objective_value - TARGET_OBJECTIVE):
            best_cube = current_best
            best_objective_value = current_best_value

        objective_values.append(best_objective_value)
        print(f"Generation {generation+1}: Best Objective Value = {best_objective_value}")

        if best_objective_value == TARGET_OBJECTIVE:
            print("Optimal solution found!")
            break

    # Menampilkan state akhir
    # display_cube(best_cube, title="Final Cube State")

    # Menampilkan hasil eksperimen (grafik perubahan nilai objektif)
    plt.plot(objective_values, marker='o')
    plt.title("Objective Value Progression")
    plt.xlabel("Generation")
    plt.ylabel("Best Objective Value")
    plt.show()

if __name__ == "__main__":
    genetic_algorithm_with_visualization()
