import re
from typing import List

def is_bored(str_arg: str) -> int:
    segments: List[str] = re.split(r'[.?!]\s*', str_arg)
    tally: int = 0
    counter_index: int = 0
    while counter_index < len(segments):
        current_chunk: str = segments[counter_index]
        if not current_chunk.startswith('I '):
            counter_index += 1
            continue
        tally += 1
        counter_index += 1
    return tally