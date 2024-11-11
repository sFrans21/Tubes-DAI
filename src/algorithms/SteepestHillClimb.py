# File: SteepestHillClimb.py
import sys
import os
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

from cube.Magiccube import MagicCube

# Class SteepestHillClimbing untuk mencari solusi dari kubus dengan algoritma Steepest Ascent Hill Climbing
class SteepestHillClimbing:
    # Inisialisasi kubus, skor awal, dan maksimum iterasi
    def __init__(self, max_iterations=1000):
        self.solver = MagicCube()
        self.initial_state = self.solver.cube
        self.objective_function = self.solver.fitness(self.initial_state)
        self.max_iterations = max_iterations
        self.history = []

    # Mencari solusi dari kubus
    def search(self):
        iteration_count = 1
        start_time = time.time()

        # Mencari tetangga terbaik dari kubus
        while iteration_count <= self.max_iterations:
            neighbors = self.solver.neighbors_function(self.initial_state)
            best_neighbor = min(neighbors, key=self.solver.fitness)
            best_score = self.solver.fitness(best_neighbor)
            
            # Mengganti kubus awal dengan kubus tetangga terbaik
            if best_score < self.objective_function:
                self.initial_state = best_score
                self.objective_function = best_score
                self.history.append(self.objective_function)
                print(f"Iterasi {iteration_count}: Skor sekarang = {self.objective_function}")
                
                if self.is_solved(self.objective_function):
                    break

            else:
                break
            
            iteration_count += 1

        execute_time = time.time() - start_time
        return self.initial_state, self.objective_function, execute_time, self.history, iteration_count

    # Mengecek apakah kubus sudah selesai
    def is_solved(self, score):
        return score == 0

# if __name__ == "__main__":
#     main = SteepestHillClimbing(max_iterations=100)
#     print("Visualisasi kubus dari bawah ke atas, jadinya bayangkan tiap lapisan ditumpuk saja")
#     print("Kubus awal (random):")
#     print(main.initial_state)
#     print("Skor awal:", main.objective_function)

#     final_state, final_score, execute_time, history = main.search()
#     print("Skor akhir:", final_score)
#     print("Kubus akhir:")
#     print(final_state)

#     import matplotlib.pyplot as plt

#     # Visualisasi skor tiap iterasi
#     plt.plot(history)
#     plt.xlabel('Iteration')
#     plt.ylabel('Score')
#     plt.title('Score per Iteration')
#     plt.show()