from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# Inisialisasi FastAPI
app = FastAPI()

# Model input untuk API
class CubeInput(BaseModel):
    size: int  # Ukuran kubus (n)
    algorithm: str  # Algoritma yang digunakan
    iterations: int  # Jumlah iterasi yang dijalankan

# Endpoint API untuk menerima input dan menjalankan algoritma
@app.post("/solve_magic_cube/")
def solve_magic_cube(input_data: CubeInput):
    # Placeholder: Panggil fungsi algoritma yang sesuai di sini
    result = {
        "size": input_data.size,
        "algorithm": input_data.algorithm,
        "iterations": input_data.iterations,
        "solution": "Dummy solution - Implementasikan algoritma di sini"
    }
    return result

# Endpoint tes untuk memastikan API berjalan
@app.get("/")
def read_root():
    return {"message": "Magic Cube API is running!"}