# Steepest Hill Climbing Algorithm
import time
from magiccube import MagicCube

class SteepestHillClimbing:
    def __init__(self, max_iterations=1000):
        self.solver = MagicCube()
        self.initial_state = self.solver.cube
        self.objective_function = self.solver.fitness(self.initial_state)
        self.max_iterations = max_iterations

    def search(self):
        iteration_count = 1
        start_time = time.time()

        # swap_number
        while iteration_count <= self.max_iterations:
            neighbors = self.solver.neighbors_function(self.initial_state)
            best_neighbor = None
            best_score = self.objective_function            
            
            for neighbor in neighbors:
                neighbor_score = self.solver.fitness(neighbor)
                if neighbor_score < best_score:
                    best_score = neighbor_score
                    best_neighbor = neighbor

            if best_neighbor is None:
                break

            self.initial_state = best_neighbor
            self.objective_function = best_score
            print(f"Iterasi {iteration_count}: Skor sekarang = {self.objective_function}")
            
            if self.is_solved(self.objective_function):
                break
            
            iteration_count += 1

        end_time = time.time()
        print(f"Waktu yang dibutuhkan: {end_time - start_time} detik")
        return self.initial_state, self.objective_function

    def is_solved(self, score):
        return score == 0

main = SteepestHillClimbing(max_iterations=100)
print("Visualisasi kubus dari bawah ke atas, jadinya bayangkan tiap lapisan ditumpuk saja")
print("Kubus awal (random):")
print(main.initial_state)
print("Skor awal:", main.objective_function)

final_state, final_score = main.search()
print("Skor akhir:", final_score)
print("Kubus akhir:")
print(final_state)