import re
from typing import List

def is_bored(input_string: str) -> int:
    temp_array: List[str] = re.split(r'[.?!]\s*', input_string)
    total_matches: int = 0
    for fragment in temp_array:
        if fragment.startswith('I '):
            total_matches += 1
    return total_matches