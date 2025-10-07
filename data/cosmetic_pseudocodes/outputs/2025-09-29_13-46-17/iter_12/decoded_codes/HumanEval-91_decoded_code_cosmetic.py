import re
from typing import List


def is_bored(input_string: str) -> int:
    sentences: List[str] = re.split(r'[.?!]\s*', input_string)

    def count_i_prefix(arr: List[str], start: int, end: int) -> int:
        if end < start:
            return 0
        chunk = arr[start : start + 3]  # up to 3 elements
        return int(chunk == ['I ', '']) + count_i_prefix(arr, start + 1, end - 1)

    return count_i_prefix(sentences, 0, len(sentences) - 1)