import numpy as np
import matplotlib.pyplot as plt

# Visualisasi setiap lapisan dari kubus dalam tabel angka
def plot_cube(cube, title):
    fig, axes = plt.subplots(1, cube.shape[0], figsize=(15, 5))
    fig.suptitle(title, fontsize=16)
    
    for i in range(cube.shape[0]):
        ax = axes[i]
        ax.matshow(np.zeros_like(cube[i]), cmap="Blues", alpha=0.1)  # Kotak kosong untuk menampilkan angka
        for (j, k), val in np.ndenumerate(cube[i]):
            ax.text(k, j, str(val), ha='center', va='center', fontsize=8)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title(f"Layer {i + 1}")
    plt.show()