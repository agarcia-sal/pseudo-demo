from typing import List

def f(param_x: int) -> List[int]:
    accumulator: List[int] = []
    index_y: int = 1

    while index_y <= param_x:
        if index_y % 2 == 0:
            temp_val: int = 1
            index_z: int = 1

            while index_z <= index_y:
                temp_val *= index_z
                index_z += 1

            accumulator.append(temp_val)
        else:
            temp_sum: int = 0
            index_w: int = 1

            while index_w <= index_y:
                temp_sum += index_w
                index_w += 1

            accumulator.append(temp_sum)

        index_y += 1

    return accumulator