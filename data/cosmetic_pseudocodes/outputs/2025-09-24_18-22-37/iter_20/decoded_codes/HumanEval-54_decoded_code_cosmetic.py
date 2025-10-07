from typing import Set

def same_chars(param_alpha: str, param_beta: str) -> bool:
    index_one: int = 0
    collection_x: Set[str] = set()
    collection_y: Set[str] = set()
    length_alpha: int = len(param_alpha)
    length_beta: int = len(param_beta)

    while index_one < length_alpha:
        element_m: str = param_alpha[index_one]
        collection_x.add(element_m)
        index_one += 1

    counter_z: int = 0

    while counter_z < length_beta:
        element_n: str = param_beta[counter_z]
        collection_y.add(element_n)
        counter_z += 1

    result_flag: bool = False

    if collection_x == collection_y:
        result_flag = True
    else:
        result_flag = False

    return result_flag