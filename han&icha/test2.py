import time
import math
import random
from magiccube import MagicCube

class SimulatedAnnealing:
    def __init__(self, initial_temperature=1000, cooling_rate=0.99, temperature_threshold=0.001):
        self.solver = MagicCube()
        self.current_state = self.solver.cube
        self.current_score = self.solver.fitness(self.current_state)
        self.temperature = initial_temperature
        self.cooling_rate = cooling_rate
        self.temperature_threshold = temperature_threshold  # Ambang batas minimal suhu

    def search(self):
        iteration_count = 1
        start_time = time.time()

        while self.temperature > self.temperature_threshold:
            # Menghasilkan daftar tetangga dari state saat ini
            neighbors = self.solver.neighbors_function(self.current_state)
            
            # Memilih tetangga acak dari daftar tetangga
            next_state = random.choice(neighbors)
            next_score = self.solver.fitness(next_state)
            
            # Hitung perubahan skor (delta_E)
            delta_E = next_score - self.current_score
            probability = 1.0  # Default untuk langkah "lebih baik" (delta_E <= 0)

            # Tentukan apakah kita bergerak ke tetangga ini
            if delta_E < 0:
                # Pindah ke tetangga yang lebih baik
                self.current_state = next_state
                self.current_score = next_score
            else:
                # Hitung probabilitas untuk pindah ke tetangga yang lebih buruk
                probability = math.exp(-delta_E / self.temperature)
                # Pindah ke tetangga yang lebih buruk dengan probabilitas tertentu
                if random.random() < probability:
                    self.current_state = next_state
                    self.current_score = next_score

            # Cetak informasi iterasi, skor, suhu, dan probabilitas (jika ada langkah lebih buruk)
            print(f"Iterasi {iteration_count}: Skor Heuristik = {self.current_score}, Temperatur = {self.temperature:.4f}, Probabilitas = {probability:.4f}")

            # Jika sudah menemukan solusi sempurna (misalnya skor = 0), berhenti
            if self.is_solved(self.current_score):
                break
            
            # Turunkan temperatur
            self.temperature *= self.cooling_rate
            iteration_count += 1

        end_time = time.time()
        print(f"Waktu yang dibutuhkan: {end_time - start_time} detik")
        return self.current_state, self.current_score

    def is_solved(self, score):
        return score == 0

# Penggunaan
main = SimulatedAnnealing(initial_temperature=1000, cooling_rate=0.99, temperature_threshold=0.001)
print("Kubus awal (random):", main.current_state)
print("Skor awal:", main.current_score)

final_state, final_score = main.search()
print("Skor akhir:", final_score)
print("Kubus akhir:", final_state)