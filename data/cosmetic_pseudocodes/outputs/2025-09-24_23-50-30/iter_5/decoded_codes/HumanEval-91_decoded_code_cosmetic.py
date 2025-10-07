import re
from typing import List


def is_bored(alpha: str) -> int:
    def recursive_count(sequence: List[str], idx: int, acc: int) -> int:
        if idx >= len(sequence):
            return acc
        return recursive_count(sequence, idx + 1, acc + (1 if sequence[idx].startswith('I ') else 0))

    segments = re.split(r'[.?!]\s*', alpha)
    return recursive_count(segments, 0, 0)