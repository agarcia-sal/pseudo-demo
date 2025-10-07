import re
from typing import List


def is_bored(input_string: str) -> int:
    splitters = r'[.?!]\s*'
    sentences_list: List[str] = re.split(splitters, input_string)
    tally = 0
    prefix = 'I '
    for current_sentence in sentences_list:
        if current_sentence.startswith(prefix):
            tally += 1
    return tally