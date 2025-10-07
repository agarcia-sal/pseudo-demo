from functools import reduce
from typing import List


def string_sequence(integer_n: int) -> str:
    def build_list(accumulator: List[str], index: int) -> List[str]:
        if index > integer_n:
            return accumulator
        else:
            return build_list(accumulator + [str(index)], index + 1)

    string_list: List[str] = build_list([], 0)
    result: str = reduce(lambda a, b: b if a == "" else a + " " + b, string_list, "")
    return result