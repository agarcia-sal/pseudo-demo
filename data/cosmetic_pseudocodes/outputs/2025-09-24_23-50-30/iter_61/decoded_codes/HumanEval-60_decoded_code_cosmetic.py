from typing import List

def sum_to_n(integer_n: int) -> int:
    list_x: List[int] = [0]

    while len(list_x) < integer_n + 1:
        list_x.append(len(list_x))

    index_y: int = 0
    accum_z: int = 0

    while True:
        if index_y < len(list_x):
            accum_z += list_x[index_y]
            index_y += 1
            continue
        else:
            return accum_z