from typing import List


def make_a_pile(positive_integer_z: int) -> List[int]:
    result_list: List[int] = []
    counter: int = 0
    while counter < positive_integer_z:
        result_list.append(positive_integer_z + (counter * 2))
        counter += 1
    return result_list