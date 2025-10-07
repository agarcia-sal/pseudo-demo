import re
from typing import List


def is_bored(input_string: str) -> int:
    sentences_array: List[str] = re.split(r'[.?!]\s*', input_string)
    count_bored: int = 0
    for sentence_element in sentences_array:
        if len(sentence_element) >= 2 and sentence_element[0] == 'I' and sentence_element[1] == ' ':
            count_bored += 1
    return count_bored