import re
from typing import List


def is_bored(input_string: str) -> int:
    intermediate_sentences: List[str] = re.split(r'[.?!]\s*', input_string)

    counter_var: int = 0
    iterator_index: int = 0
    total_sentences: int = len(intermediate_sentences)

    while iterator_index < total_sentences:
        current_element: str = intermediate_sentences[iterator_index]
        prefix_substring: str = current_element[:2]
        if prefix_substring == 'I ':
            counter_var += 1
        iterator_index += 1

    return counter_var