# Cara penggunaan, saat kode dijalankan, akan muncul visualisasi kubus awal
# Silang pop up tersebut maka algoritma akan berjalan
# Setelah menunggu beberapa detik, akan muncul visualisasi kubus akhir

from tesplot import SimulatedAnnealing
from visual import plot_cube

main = SimulatedAnnealing(initial_temperature=1000, cooling_rate=0.99, temperature_threshold=0.001, stagnation_threshold=50)
initial_state = main.current_state
initial_score = main.current_score

# Visualisasi kondisi awal
plot_cube(initial_state, f"Initial State of the Cube (Score: {initial_score})")

# Menjalankan pencarian lokal
final_state, final_score = main.search()

# Visualisasi kondisi akhir
plot_cube(final_state, f"Final State of the Cube (Score: {final_score})")


# main = SimulatedAnnealing(initial_temperature=1000, cooling_rate=0.99, temperature_threshold=0.001, stagnation_threshold=50)
# print("Kubus awal (random):", main.current_state)
# print("Skor awal:", main.current_score)

# final_state, final_score = main.search()
# print("Skor akhir:", final_score)
# print("Kubus akhir:", final_state)

# # Plotting hasil objective function dan probabilitas
# main.plot_objective_function()