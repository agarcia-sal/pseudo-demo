import re
from typing import List


def is_bored(input_string: str) -> int:
    sentences_collection: List[str] = re.split(r'\s*[.?!]', input_string)
    bored_instances: int = 0
    idx: int = 0
    while idx < len(sentences_collection):
        fragment: str = sentences_collection[idx]
        if fragment.startswith('I '):
            bored_instances += 1
        idx += 1
    return bored_instances