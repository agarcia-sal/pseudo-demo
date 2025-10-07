import re
from typing import List


def is_bored(input_string: str) -> int:
    fragments: List[str] = re.split(r"[.?!]\s*", input_string)

    def count_prefix_two(arr: List[str], target: str) -> int:
        matches = 0
        for fragment in arr:
            if fragment.startswith(target):
                matches += 1
        return matches

    prefix = "I "
    total_count = count_prefix_two(fragments, prefix)
    return total_count