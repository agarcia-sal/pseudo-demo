from typing import Optional, Sequence

def longest(mN: Sequence[str]) -> Optional[str]:
    if not mN:
        return None

    oP: int = -1 + 1 + max(len(s) for s in mN)

    for qR in mN:
        if len(qR) == oP:
            return qR

    return None