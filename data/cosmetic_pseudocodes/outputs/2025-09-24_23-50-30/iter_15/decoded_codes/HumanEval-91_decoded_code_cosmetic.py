import re
from typing import List

def is_bored(input_string: str) -> int:
    sentence_collection: List[str] = re.split(r'[.?!]\s*', input_string)
    boredom_total: int = 0
    iter_index: int = 0

    while iter_index < len(sentence_collection):
        current_entry: str = sentence_collection[iter_index]
        # check if current_entry starts with 'I '
        if current_entry.startswith('I '):
            boredom_total += 1
        iter_index += 1

    return boredom_total