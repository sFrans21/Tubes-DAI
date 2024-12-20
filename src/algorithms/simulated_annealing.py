import time
import math
import random
import matplotlib.pyplot as plt
import sys
import os

sys.path.append(os.path.abspath(".."))

from cube.Magiccube import MagicCube

class SimulatedAnnealing:
    def __init__(self, initial_temperature=1000, cooling_rate=0.99, temperature_threshold=0.001, stagnation_threshold=50):
        self.solver = MagicCube()
        self.initial_state = self.solver.cube
        self.objective_function = self.solver.fitness(self.initial_state)
        self.temperature = initial_temperature
        self.cooling_rate = cooling_rate
        self.temperature_threshold = temperature_threshold
        self.stagnation_threshold = stagnation_threshold  # Jumlah iterasi tanpa perbaikan untuk dianggap "stuck"
        self.iteration_scores = []  # Untuk menyimpan skor setiap iterasi
        self.probabilities = []  # Untuk menyimpan nilai e^(-delta_E / T) pada setiap iterasi
        self.total_stuck_count = 0  # Frekuensi stuck di local optima
        self.start_time = None  # Inisialisasi untuk start_time
        self.end_time = None

    def search(self):
        iteration_count = 1
        stagnation_counter = 0  # Counter untuk mendeteksi kondisi stuck
        self.start_time = time.time()

        while self.temperature > self.temperature_threshold:
            neighbors = self.solver.neighbors_function(self.initial_state)
            next_state = random.choice(neighbors)
            next_score = self.solver.fitness(next_state)

            delta_E = next_score - self.objective_function
            probability = 1.0  # Default untuk langkah "lebih baik" (delta_E <= 0)

            if delta_E < 0:
                # Ada perbaikan skor signifikan (delta_E < 0)
                self.initial_state = next_state
                self.objective_function = next_score
                stagnation_counter = 0  # Reset counter ketika ada perbaikan
            else:
                # Langkah lebih buruk, hitung probabilitas penerimaan
                probability = math.exp(-delta_E / self.temperature)
                if random.random() < probability:
                    # Terima langkah lebih buruk
                    self.initial_state = next_state
                    self.objective_function = next_score
                # Tambah counter jika tidak ada perbaikan signifikan
                stagnation_counter += 1

            # Simpan skor heuristik dan probabilitas ke dalam daftar untuk plotting
            self.iteration_scores.append(self.objective_function)
            self.probabilities.append(probability)

            # Deteksi kondisi "stuck" di local optima
            if stagnation_counter >= self.stagnation_threshold:
                self.total_stuck_count += 1  # Tambahkan hitungan stuck local
                print(f"Stuck di local optima pada iterasi {iteration_count} dengan skor {self.objective_function}")

            print(f"Iterasi {iteration_count}: Skor Heuristik = {self.objective_function}, Temperatur = {self.temperature:.4f}, Probabilitas = {probability:.4f}")

            if self.is_solved(self.objective_function):
                break

            self.temperature *= self.cooling_rate
            iteration_count += 1

        self.end_time = time.time()
        self.execution_time = self.end_time - self.start_time
        print(f"Waktu yang dibutuhkan: {self.execution_time} detik")
        print(f"Total frekuensi stuck di local optima: {self.total_stuck_count}")
        return self.initial_state, self.objective_function, self.execution_time

    def is_solved(self, score):
        return score == 0
    
    def plot_objective_function(self):
        plt.figure(figsize=(10, 5))

        # Plotting Objective Function Value over Iterations
        plt.subplot(2, 1, 1)
        plt.plot(self.iteration_scores, label='Objective Function (Score)')
        plt.xlabel("Iteration")
        plt.ylabel("Objective Function Value (Score)")
        plt.title("Objective Function Value over Iterations in Simulated Annealing")
        plt.legend()

        plt.tight_layout()
        plt.show()

    def plot_probability(self):
        plt.figure(figsize=(10, 5))

        # Plotting Probability e^(-delta_E / T) over Iterations
        plt.subplot(2, 1, 2)
        plt.plot(self.probabilities, label='Probability (e^(-delta_E / T))', color='orange')
        plt.xlabel("Iteration")
        plt.ylabel("Probability")
        plt.title("Probability of Accepting Worse Solution over Iterations")
        plt.legend()

        plt.tight_layout()
        plt.show()
