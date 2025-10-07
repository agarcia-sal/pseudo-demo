import re
from typing import List


def is_bored(arriving_string: str) -> int:
    sentences_collection: List[str] = re.split(r'[.?!]\s*', arriving_string)
    tally: int = 0
    sampler: int = 0

    while sampler < len(sentences_collection):
        current_segment: str = sentences_collection[sampler]
        if current_segment.startswith('I '):
            tally += 1
        sampler += 1

    return tally