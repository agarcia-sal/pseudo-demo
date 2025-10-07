import re
from typing import List


def is_bored(string_input: str) -> int:
    sentences_list: List[str] = re.split(r'[.?!]\s*', string_input)
    count_bored: int = 0
    index_counter: int = 0
    while index_counter < len(sentences_list):
        current_sentence: str = sentences_list[index_counter]
        if current_sentence.startswith('I '):
            count_bored += 1
        index_counter += 1
    return count_bored