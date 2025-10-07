from typing import List


def all_prefixes(input_string: str) -> List[str]:
    def helper(i: int, acc: List[str]) -> List[str]:
        if i < 0:
            return acc
        else:
            return helper(i - 1, [input_string[: i + 1]] + acc)

    return helper(len(input_string) - 1, [])