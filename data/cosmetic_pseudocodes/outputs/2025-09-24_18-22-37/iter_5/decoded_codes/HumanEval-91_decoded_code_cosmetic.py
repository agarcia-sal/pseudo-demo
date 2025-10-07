import re
from typing import List


def is_bored(string_input: str) -> int:
    sentences_array: List[str] = re.split(r'[.?!]\s*', string_input)
    boredom_tally: int = 0
    idx: int = 0
    while idx < len(sentences_array):
        current_sentence: str = sentences_array[idx]
        if len(current_sentence) >= 2 and current_sentence[0] == 'I' and current_sentence[1] == ' ':
            boredom_tally += 1
        idx += 1
    return boredom_tally