import re
from typing import List


def is_bored(message: str) -> int:
    segments: List[str] = re.split(r'[.?!]\s*', message)

    def count_bored(seg_list: List[str], idx: int, acc: int) -> int:
        if idx >= len(seg_list):
            return acc
        if seg_list[idx].startswith('I '):
            return count_bored(seg_list, idx + 1, acc + 1)
        return count_bored(seg_list, idx + 1, acc)

    return count_bored(segments, 0, 0)