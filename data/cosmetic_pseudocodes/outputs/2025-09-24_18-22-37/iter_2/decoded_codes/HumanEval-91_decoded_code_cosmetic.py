import re
from typing import List


def is_bored(text: str) -> int:
    sentences_array: List[str] = re.split(r'[.?!]\s*', text)
    count_bored_instances: int = 0
    for element in sentences_array:
        if element.startswith('I '):
            count_bored_instances += 1
    return count_bored_instances