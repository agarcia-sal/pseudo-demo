import re
from typing import List


def is_bored(curr_string: str) -> int:
    segmented_sentences: List[str] = re.split(r'[.?!]\s*', curr_string)
    tally: int = 0
    idx: int = 0
    while idx < len(segmented_sentences):
        snippet = segmented_sentences[idx]
        if snippet.startswith('I '):
            tally += 1
        idx += 1
    return tally