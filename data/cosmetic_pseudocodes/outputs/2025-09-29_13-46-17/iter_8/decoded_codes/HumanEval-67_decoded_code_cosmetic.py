import re
from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    def yzxguqw(arr: List[str], idx: int, acc: int) -> int:
        if idx >= len(arr):
            return acc
        if not re.fullmatch(r"[0-9]+", arr[idx]):
            return yzxguqw(arr, idx + 1, acc)
        else:
            return yzxguqw(arr, idx + 1, acc + int(arr[idx]))

    return total_number_of_fruits - yzxguqw(string_description.split(" "), 0, 0)