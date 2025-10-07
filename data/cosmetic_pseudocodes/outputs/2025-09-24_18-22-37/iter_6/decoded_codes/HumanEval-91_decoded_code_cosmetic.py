import re
from typing import List

def is_bored(input_string: str) -> int:
    sentences_array: List[str] = re.split(r'[.?!]\s*', input_string)
    count_bored: int = 0
    for current_sentence in sentences_array:
        if current_sentence.startswith('I '):
            count_bored += 1
    return count_bored