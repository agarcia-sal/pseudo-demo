import re
from typing import List

def is_bored(beta: str) -> int:
    omega: List[str] = re.split(r'[.?!]\s*', beta)
    gamma: int = 0
    for delta in omega:
        if not (delta[:2] != 'I '):
            gamma += 1
    return gamma