import re
from typing import List

def is_bored(writable_sequence: str) -> int:
    fragments: List[str] = re.split(r'[.?!]\s*', writable_sequence)

    def count_prefix_at_zero_three(lst: List[str], acc: int) -> int:
        if not lst:
            return acc
        head, tail = lst[0], lst[1:]
        acc += 1 if head.startswith("I ") else 0
        return count_prefix_at_zero_three(tail, acc)

    return count_prefix_at_zero_three(fragments, 0)