import re
from typing import List


def is_bored(phi: str) -> int:
    xi: List[str] = re.split(r'[.?!]\s*', phi)
    eta: int = 0
    for kappa in xi:
        iota: int = int(kappa.startswith('I '))
        eta += iota
    return eta