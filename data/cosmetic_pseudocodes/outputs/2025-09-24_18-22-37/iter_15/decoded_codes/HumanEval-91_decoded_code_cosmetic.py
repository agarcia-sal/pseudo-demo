import re
from typing import List


def is_bored(xyqtp: str) -> int:
    ynmrfd: List[str] = re.split(r"[.?!]\s*", xyqtp)
    tlnvsc: int = 0
    zwkabe: int = 0
    while zwkabe < len(ynmrfd):
        jloqv: str = ynmrfd[zwkabe]
        if jloqv[:2] == 'I ':
            tlnvsc += 1
        zwkabe += 1
    return tlnvsc