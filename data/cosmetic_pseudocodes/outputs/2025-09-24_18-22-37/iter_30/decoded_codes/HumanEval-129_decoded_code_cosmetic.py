from typing import List


def minPath(matrix: List[List[int]], alpha: int) -> List[int]:
    size: int = len(matrix)
    minimum_value: int = size * size + 1
    row_index: int = 0

    while row_index < size:
        col_index: int = 0
        while col_index < size:
            if matrix[row_index][col_index] == 1:
                neighbors: List[int] = []
                if row_index != 0:
                    neighbors.append(matrix[row_index - 1][col_index])
                if col_index != 0:
                    neighbors.append(matrix[row_index][col_index - 1])
                if row_index != size - 1:
                    neighbors.append(matrix[row_index + 1][col_index])
                if col_index != size - 1:
                    neighbors.append(matrix[row_index][col_index + 1])
                if neighbors:
                    current_min: int = neighbors[0]
                    pointer: int = 1
                    while pointer < len(neighbors):
                        if neighbors[pointer] < current_min:
                            current_min = neighbors[pointer]
                        pointer += 1
                    minimum_value = current_min
            col_index += 1
        row_index += 1

    output_sequence: List[int] = []
    counter: int = 0
    while counter < alpha:
        if counter % 2 == 0:
            output_sequence.append(1)
        else:
            output_sequence.append(minimum_value)
        counter += 1

    return output_sequence