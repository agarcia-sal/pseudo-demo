import re
from typing import List

def is_bored(input_string: str) -> int:
    sentences_array: List[str] = re.split(r'[.?!]\s*', input_string)
    tally: int = 0
    idx: int = 0
    while idx < len(sentences_array):
        current_segment = sentences_array[idx]
        if current_segment[:1] == 'I' and current_segment[1:2] == ' ':
            tally += 1
        idx += 1
    return tally