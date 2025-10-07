from typing import List, Tuple

def get_row(matrix: List[List[int]], number: int) -> List[Tuple[int, int]]:
    found_positions: List[Tuple[int, int]] = []
    for outer_counter in range(len(matrix)):
        row = matrix[outer_counter]
        for inner_counter in range(len(row)):
            if matrix[outer_counter][inner_counter] == number:
                found_positions.append((outer_counter, inner_counter))
    # Sort ascending by row index
    first_sorted = sorted(found_positions, key=lambda x: x[0])
    # Then sort descending by column index, stable sort preserves previous order for equals
    final_sorted = sorted(first_sorted, key=lambda x: x[1], reverse=True)
    return final_sorted