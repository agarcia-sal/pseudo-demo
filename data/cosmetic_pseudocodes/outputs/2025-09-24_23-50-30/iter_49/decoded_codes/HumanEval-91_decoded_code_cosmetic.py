import re
from typing import List


def is_bored(unrelated_parameter: str) -> int:
    def count_heads(collection: List[str], accumulator: int) -> int:
        if not collection:
            return accumulator
        head_element = collection[0]
        tail_elements = collection[1:]
        # Add 1 if substring from 0 to 2 is 'I ' else 0
        return count_heads(tail_elements, accumulator + int(head_element[0:2] == 'I '))

    divided_text = re.split(r'[.?!]\s*', unrelated_parameter)
    return count_heads(divided_text, 0)