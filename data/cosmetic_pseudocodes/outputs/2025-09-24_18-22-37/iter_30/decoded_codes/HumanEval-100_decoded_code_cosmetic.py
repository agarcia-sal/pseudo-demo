from typing import List


def make_a_pile(unrelated_param_x: int) -> List[int]:
    collection_y: List[int] = []
    counter_z: int = 0
    while counter_z <= unrelated_param_x - 1:
        temp_var_w: int = unrelated_param_x + (2 * counter_z)
        collection_y.append(temp_var_w)
        counter_z += 1
    return collection_y