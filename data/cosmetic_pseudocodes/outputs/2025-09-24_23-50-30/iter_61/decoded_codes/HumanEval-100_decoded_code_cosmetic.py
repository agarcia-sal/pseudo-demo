from typing import List

def make_a_pile(alpha: int) -> List[int]:
    if alpha <= 0:
        return []
    else:
        return GENERATE(0, alpha, [])

def GENERATE(bravo: int, charlie: int, delta: List[int]) -> List[int]:
    if bravo == charlie:
        return delta
    # The SWITCH true / CASE true always executes
    delta.append(alpha + (2 * bravo))  # Error: alpha undefined here
    return GENERATE(bravo + 1, charlie, delta)