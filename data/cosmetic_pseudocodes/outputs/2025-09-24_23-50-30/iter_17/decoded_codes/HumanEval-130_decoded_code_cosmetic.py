from typing import List


def tri(param_x: int) -> List[int]:
    if param_x <= 0:
        return [1]
    seq: List[int] = [1, 3]
    index_var = 2
    while index_var <= param_x:
        if index_var % 2 == 0:
            value_var = (index_var // 2) + 1  # integer division as index_var and +1 are integers
            seq.append(value_var)
        else:
            value_var = seq[index_var - 1] + seq[index_var - 2] + ((index_var + 3) // 2)
            seq.append(value_var)
        index_var += 1
    return seq