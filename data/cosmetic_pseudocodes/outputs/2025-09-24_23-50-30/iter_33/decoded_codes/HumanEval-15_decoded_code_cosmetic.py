from functools import reduce
from typing import List


def string_sequence(integer_p: int) -> str:
    def build_list(current_x: int, limit_y: int, acc_z: List[str]) -> List[str]:
        if current_x > limit_y:
            return acc_z
        else:
            return build_list(current_x + 1, limit_y, acc_z + [str(current_x)])

    collected_list: List[str] = build_list(0, integer_p, [])
    concatenated_result: str = reduce(lambda a, b: a + " " + b, collected_list)
    return concatenated_result