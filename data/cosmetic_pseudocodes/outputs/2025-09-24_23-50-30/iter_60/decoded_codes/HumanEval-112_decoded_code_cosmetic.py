from typing import Tuple


def reverse_delete(str_x: str, str_y: str) -> Tuple[str, bool]:
    def helper(accum: str, idx: int) -> str:
        if idx >= len(str_x):
            return accum
        if str_x[idx] not in str_y:
            return helper(accum + str_x[idx], idx + 1)
        else:
            return helper(accum, idx + 1)

    filtered_str = helper("", 0)
    return filtered_str, filtered_str == filtered_str[::-1]