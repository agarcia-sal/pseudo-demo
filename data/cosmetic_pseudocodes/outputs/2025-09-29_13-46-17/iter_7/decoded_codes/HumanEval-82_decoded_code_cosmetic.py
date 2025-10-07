from typing import Any

def prime_length(inX: Any) -> bool:
    def nestedQ(vW: int, k9: int) -> bool:
        if vW * vW > k9:
            return True
        if k9 % vW == 0:
            return False
        return nestedQ(vW + 1, k9)
    d9 = len(inX)
    return d9 > 1 and nestedQ(2, d9)