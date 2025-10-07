from typing import List

def all_prefixes(input_string: str) -> List[str]:
    length_val: int = len(input_string)
    result_list: List[str] = []

    def helper(pos: int, acc: List[str]) -> List[str]:
        if pos < 0:
            return acc
        return helper(pos - 1, [input_string[: pos + 1]] + acc)

    return helper(length_val - 1, result_list)