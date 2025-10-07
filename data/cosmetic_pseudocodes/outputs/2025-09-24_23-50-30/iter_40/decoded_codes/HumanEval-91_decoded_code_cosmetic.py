import re
from typing import List


def is_bored(input_string: str) -> int:
    temp_storage: List[str] = re.split(r'[.?!]\s*', input_string)
    accumulator: int = 0
    for element in temp_storage:
        if element.startswith('I '):
            accumulator += 1
    return accumulator