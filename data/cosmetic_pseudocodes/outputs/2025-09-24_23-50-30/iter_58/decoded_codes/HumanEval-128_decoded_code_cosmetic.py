from typing import List, Optional

def prod_signs(w: List[int]) -> Optional[int]:
    if len(w) == 0:
        return None
    if 0 in w:
        a = 0
    else:
        b = sum(1 for c in w if c < 0)
        a = 1
        while b > 0:
            a *= -1
            b -= 1
    d = sum(e if e >= 0 else -e for e in w)
    return a * d