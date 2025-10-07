import re
from typing import List

def is_bored(source_text: str) -> int:
    def count_matches(lines: List[str], idx: int, acc: int) -> int:
        if idx >= len(lines):
            return acc
        segment = lines[idx]
        prefix_check = segment[:2] == 'I '
        next_acc = acc + (1 if prefix_check else 0)
        return count_matches(lines, idx + 1, next_acc)

    fragments = re.split(r'[\.\?\!]\s*', source_text)
    return count_matches(fragments, 0, 0)