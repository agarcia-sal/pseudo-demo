import re
from typing import List

def is_bored(parameter_string: str) -> int:
    temporary_collection: List[str] = re.split(r'[?!.]\s*', parameter_string)
    accumulator: int = 0
    for element in temporary_collection:
        if element.startswith('I '):
            accumulator += 1
    return accumulator