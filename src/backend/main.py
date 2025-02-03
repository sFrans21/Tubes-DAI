# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List
# from src.algorithms.simulated_annealing import run_simulated_annealing  # Misalnya ini untuk SA
# from src.algorithms.SteepestHillClimb import run_steepest_ascent  # Misalnya untuk Hill Climbing
# from src.algorithms.genetic import run_genetic_algorithm  # Misalnya untuk Genetic Algorithm

# # Inisialisasi FastAPI
# app = FastAPI()

# # Model input untuk API
# class CubeInput(BaseModel):
#     size: int  # Ukuran kubus (n)
#     algorithm: str  # Algoritma yang digunakan
#     # iterations: int  # Jumlah iterasi yang dijalankan

# # Endpoint API untuk menerima input dan menjalankan algoritma
# @app.post("/solve_cube")
# async def solve_cube(input: CubeInput):
#     # Berdasarkan input, pilih algoritma yang digunakan
#     if input.algorithm == "genetic":
#         result = run_genetic_algorithm(input.size)
#     elif input.algorithm == "hill_climbing":
#         result = run_steepest_ascent(input.size)
#     elif input.algorithm == "simulated_annealing":
#         result = run_simulated_annealing(input.size)
#     else:
#         return {"error": "Algorithm not supported"}

#     return {"result": result}

# # # Endpoint tes untuk memastikan API berjalan
# # @app.get("/")
# # def read_root():
# #     return {"message": "Magic Cube API is running!"}




from fastapi import FastAPI
from pydantic import BaseModel
import sys
print(sys.path)  # Memeriksa apakah folder 'src' ada di dalam sys.path

import os

# Menambahkan path ke direktori 'src' agar modul 'src' dapat ditemukan
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

from src.algorithms.genetic import genetic_algorithm  # Mengimpor fungsi genetic_algorithm dari file genetic.py

app = FastAPI()

# Model untuk menerima input dari frontend
class CubeInput(BaseModel):
    population_size: int
    iterations: int

@app.post("/solve_cube")
async def solve_cube(input: CubeInput):
    # Memanggil fungsi genetic_algorithm dengan parameter dari input frontend
    result = genetic_algorithm(input.iterations, input.population_size)
    
    return {"result": result}
