def hill_climbing_with_sideways(cube, magic_number, max_sideways=100):
    current_cube = cube.copy()
    current_score = objective_function(current_cube, magic_number)
    sideways_moves = 0
    
    while True:
        next_cube = swap_positions(current_cube.copy())
        next_score = objective_function(next_cube, magic_number)
        
        if next_score < current_score:
            current_cube = next_cube
            current_score = next_score
            sideways_moves = 0  # Reset sideways move
        elif next_score == current_score and sideways_moves < max_sideways:
            current_cube = next_cube
            sideways_moves += 1  # Hitung sideways move
        else:
            break  # Berhenti jika tidak ada perbaikan dan sideways sudah maksimal
    
    return current_cube, current_score
