import re
from typing import List


def is_bored(input_string: str) -> int:
    temp_collection: List[str] = re.split(r'[.?!]\s*', input_string)
    total: int = 0
    for element in temp_collection:
        if element.startswith('I '):
            total += 1
    return total