# Cara penggunaan, saat kode dijalankan, akan muncul visualisasi kubus awal
# Silang pop up tersebut maka algoritma akan berjalan
# Setelah menunggu beberapa detik, akan muncul visualisasi kubus akhir

from algorithms.SteepestHillClimb import SteepestHillClimbing
from visual import plot_cube

main = SteepestHillClimbing(max_iterations=100)
initial_state = main.initial_state
initial_score = main.objective_function

# Visualisasi kondisi awal
plot_cube(initial_state, f"Initial State of the Cube (Score: {initial_score})")

# Menjalankan pencarian lokal
final_state, final_score, execution_time = main.search()

# Visualisasi kondisi akhir
plot_cube(final_state, f"Final State of the Cube (Score: {final_score}, Time: {execution_time:.2f} seconds)")