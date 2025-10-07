from typing import List


def concatenate(list_of_strings: List[str]) -> str:
    def helper(index: int, acc: str) -> str:
        if index >= len(list_of_strings):
            return acc
        else:
            return helper(index + 1, acc + list_of_strings[index])

    return helper(0, "")