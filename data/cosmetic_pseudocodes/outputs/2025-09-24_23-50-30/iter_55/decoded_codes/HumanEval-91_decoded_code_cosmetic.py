import re
from typing import List


def is_bored(alpha: str) -> int:
    beta: List[str] = re.split(r'[?!.]\s*', alpha)
    gamma: int = 0
    for delta in beta:
        if delta.startswith('I '):
            gamma += 1
    return gamma