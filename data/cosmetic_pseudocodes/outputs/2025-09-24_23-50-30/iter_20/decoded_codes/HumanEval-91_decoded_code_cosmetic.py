import re
from typing import List


def is_bored(task_string: str) -> int:
    segments_collection: List[str] = re.split(r'[?!.]\s*', task_string)
    tally: int = 0
    for segment in segments_collection:
        if segment[:2] == 'I ':
            tally += 1
    return tally