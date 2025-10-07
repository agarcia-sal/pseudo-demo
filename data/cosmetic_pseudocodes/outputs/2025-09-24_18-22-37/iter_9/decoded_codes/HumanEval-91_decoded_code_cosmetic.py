import re
from typing import Union

def is_bored(u: str) -> int:
    sentences = re.split(r'[.?!]\s*', u)
    temp_result = 0
    for s in sentences:
        prefix = s[:2]
        if prefix == 'I ':
            temp_result += 1
    return temp_result