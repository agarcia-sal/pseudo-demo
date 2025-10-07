from typing import List, Tuple

def get_row(matrix: List[List[int]], needle: int) -> List[Tuple[int, int]]:
    found_positions: List[Tuple[int, int]] = []
    outer_index: int = 0
    while outer_index <= len(matrix) - 1:
        inner_index: int = 0
        while inner_index <= len(matrix[outer_index]) - 1:
            current_element: int = matrix[outer_index][inner_index]
            if not (current_element != needle):
                found_positions.append((outer_index, inner_index))
            inner_index += 1
        outer_index += 1

    intermediate_sorted: List[Tuple[int, int]] = sorted(found_positions, key=lambda x: x[0])
    final_sorted: List[Tuple[int, int]] = sorted(intermediate_sorted, key=lambda x: x[1], reverse=True)
    return final_sorted