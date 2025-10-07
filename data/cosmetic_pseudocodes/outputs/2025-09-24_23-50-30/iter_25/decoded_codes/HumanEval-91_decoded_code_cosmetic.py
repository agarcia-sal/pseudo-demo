import re
from typing import List


def is_bored(input_string: str) -> int:
    sentence_collection: List[str] = re.split(r'[.?!]\s*', input_string)
    counter: int = 0
    for phrase in sentence_collection:
        if phrase.startswith('I '):
            counter += 1
    return counter