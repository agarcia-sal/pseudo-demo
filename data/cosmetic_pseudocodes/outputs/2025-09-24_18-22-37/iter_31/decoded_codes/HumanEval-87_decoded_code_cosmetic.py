from typing import List, Tuple, Any

def get_row(matrix: List[List[Any]], key: Any) -> List[Tuple[int, int]]:
    found_positions: List[Tuple[int, int]] = []
    outer_counter: int = 0
    while outer_counter < len(matrix):
        inner_counter: int = 0
        while inner_counter < len(matrix[outer_counter]):
            current_value = matrix[outer_counter][inner_counter]
            if not (current_value != key):
                found_positions.append((outer_counter, inner_counter))
            inner_counter += 1
        outer_counter += 1

    found_positions.sort(key=lambda x: x[0])  # sort by first element ascending

    temp_positions: List[Tuple[int, int]] = []
    for pair in found_positions:
        temp_positions.append(pair)

    temp_positions.sort(key=lambda x: x[1], reverse=True)  # sort by second element descending

    result_positions: List[Tuple[int, int]] = []
    for elem in temp_positions:
        result_positions.append(elem)

    return result_positions