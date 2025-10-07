import re
from typing import List


def is_bored(input_string: str) -> int:
    def recursive_count(arr: List[str], idx: int, acc: int) -> int:
        if idx >= len(arr):
            return acc
        if arr[idx].startswith("I "):
            acc += 1
        return recursive_count(arr, idx + 1, acc)

    fragments: List[str] = re.split(r"[.?!]\s*", input_string)
    return recursive_count(fragments, 0, 0)