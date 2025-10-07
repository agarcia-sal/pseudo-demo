from typing import Sequence

def triples_sum_to_zero(collection: Sequence[int]) -> bool:
    n = len(collection)
    pos_x = 0
    while pos_x < n - 2:
        pos_y = pos_x + 1
        while pos_y < n - 1:
            pos_z = pos_y + 1
            while pos_z < n:
                if collection[pos_x] + collection[pos_y] + collection[pos_z] == 0:
                    return True
                pos_z += 1
            pos_y += 1
        pos_x += 1
    return False