import re
from typing import List


def is_bored(opaque_string: str) -> int:
    intermediate_collection: List[str] = re.split(r'[.?!]\s*', opaque_string)
    accumulator: int = 0
    for item in intermediate_collection:
        if item.startswith('I '):
            accumulator += 1
    return accumulator