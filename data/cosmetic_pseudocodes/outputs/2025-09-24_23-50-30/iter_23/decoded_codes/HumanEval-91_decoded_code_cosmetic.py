import re
from typing import List


def is_bored(text_parameter: str) -> int:
    fragment_collection: List[str] = re.split(pattern=r'[?!.]\s*', string=text_parameter)
    tally: int = 0
    for element in fragment_collection:
        if element.startswith('I '):
            tally += 1
    return tally