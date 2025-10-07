import re
from typing import List


def is_bored(x: str) -> int:
    a: List[str] = re.split(r"[.?!]\s*", x)

    def z(p: int, q: int, r: int) -> int:
        if p < q:
            # Check if first two characters of a[p] are 'I '
            r += int(a[p][:2] == 'I ')
            return z(p + 1, q, r)
        else:
            return r

    return z(0, len(a), 0)