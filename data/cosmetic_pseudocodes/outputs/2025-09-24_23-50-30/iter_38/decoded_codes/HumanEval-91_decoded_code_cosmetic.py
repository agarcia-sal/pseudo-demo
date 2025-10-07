import re
from typing import Union


def is_bored(alpha: str) -> int:
    beta = re.split(r'\s*[.?!]', alpha)
    gamma = 0
    for delta in beta:
        if delta.startswith('I '):
            gamma += 1
    return gamma