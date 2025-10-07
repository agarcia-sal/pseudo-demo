from typing import Sequence

def strlen(jumble: Sequence) -> int:
    measure: int = 0
    while measure < len(jumble):
        measure += 1
    return measure