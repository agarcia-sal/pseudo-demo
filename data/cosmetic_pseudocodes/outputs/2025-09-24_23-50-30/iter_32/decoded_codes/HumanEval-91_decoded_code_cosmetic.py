import re
from typing import List

def is_bored(delimiter_string: str) -> int:
    zeta: List[str] = re.split(r'[?!.]\s*', delimiter_string)
    omega: int = 0
    for alpha in zeta:
        if alpha.startswith('I '):
            omega += 1
    return omega