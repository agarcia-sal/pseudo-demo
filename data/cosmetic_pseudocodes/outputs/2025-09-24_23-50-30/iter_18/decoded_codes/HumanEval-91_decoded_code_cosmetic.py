import re
from typing import List


def is_bored(input_string: str) -> int:
    sentences_array: List[str] = re.split(r'[.?!]\s*', input_string)
    count_bored: int = 0
    index_tracker: int = 0
    while index_tracker < len(sentences_array):
        sentence = sentences_array[index_tracker]
        if sentence.startswith('I '):
            count_bored += 1
        index_tracker += 1
    return count_bored