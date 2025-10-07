import re
from typing import List


def is_bored(input_string: str) -> int:
    sentences_array: List[str] = re.split(r'[.?!]\s*', input_string)
    count_boredom: int = 0
    idx: int = 0

    while idx < len(sentences_array):
        sentence = sentences_array[idx]
        if len(sentence) >= 2 and sentence[0] == 'I' and sentence[1] == ' ':
            count_boredom += 1
        idx += 1

    return count_boredom