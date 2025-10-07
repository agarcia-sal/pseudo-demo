from typing import List, Tuple, Any


def get_row(matrix: List[List[Any]], key: Any) -> List[Tuple[int, int]]:
    accumulator: List[Tuple[int, int]] = []
    i = 0
    while i <= len(matrix) - 1:
        j = 0
        while j <= len(matrix[i]) - 1:
            if matrix[i][j] == key:
                pair = (i, j)
                accumulator.append(pair)
            j += 1
        i += 1

    temp1 = accumulator
    temp2: List[Tuple[int, int]] = []
    for _ in range(len(temp1)):
        for inner_index in range(len(temp1) - 1):
            if temp1[inner_index][1] < temp1[inner_index + 1][1]:
                swap_a = temp1[inner_index]
                swap_b = temp1[inner_index + 1]
                temp1[inner_index] = swap_b
                temp1[inner_index + 1] = swap_a

    temp3 = temp1
    for _ in range(len(temp3)):
        for q in range(len(temp3) - 1):
            if not (temp3[q][0] < temp3[q + 1][0]):
                swap_x = temp3[q]
                swap_y = temp3[q + 1]
                temp3[q] = swap_y
                temp3[q + 1] = swap_x

    return temp3