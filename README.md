# Tubes-DAI

Implementation of machine learning algorithms to find the optimal configuration of a **5×5×5 Magic Cube**.

## Table of Contents
- [Brief Description](#brief-description)
- [Setup and Run Instructions](#setup-and-run-instructions)
- [Task Distribution](#task-distribution)

## Brief Description
The main component of this repository is the **`src`** directory. This folder contains all code implementations of the algorithms used in this project.

- The **`cube`** directory contains the implementation of the Magic Cube structure.
- The **`algorithms`** directory contains the implementations of the three algorithms used in this project:
  - Simulated Annealing
  - Steepest Ascent Hill-Climbing
  - Genetic Algorithm

These algorithms are used to search for the best configuration of a **5×5×5 Magic Cube**.

## Setup and Run Instructions

1. Clone this repository to your computer manually, or open a terminal/command prompt and run:

```bash
git clone https://github.com/sFrans21/Tubes-DAI.git
```

2. Navigate to the cloned project directory.

3. Move to the **`algorithms`** folder.

4. Run each algorithm using the following command:

```bash
python [algorithm_filename].py
```

Example:

```bash
python genetic.py
```

## Task Distribution

| Team Member | Responsibilities |
|-------------|------------------|
| **Hanan Fitra Salam / 18222133** | Implementation of the **Simulated Annealing plotting component**; Report: Experimental results of Simulated Annealing; Conclusion and recommendations |
| **Salsabila Azzahra / 18222139** | Implementation of the **Simulated Annealing algorithm process**; Report: Explanation of the Simulated Annealing implementation |
| **Samuel Franciscus T.H / 18222131** | Implementation of **genetic.py** and **gencube.py** (Magic Cube for Genetic Algorithm); Report: Objective function selection; Explanation of the Genetic Algorithm; Experimental results and analysis of the Genetic Algorithm; README.md |
| **M. Reffy Haykal / 18222103** | Implementation of **Magiccube.py** (for Steepest Ascent Hill-Climbing and Simulated Annealing), **SteepestHillClimb.py**, and **visual.py**; Report: Explanation of the Magic Cube implementation; Explanation of the Steepest Ascent Hill-Climbing implementation |
