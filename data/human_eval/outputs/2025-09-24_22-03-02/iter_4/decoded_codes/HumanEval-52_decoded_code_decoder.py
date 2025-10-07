from typing import List

def below_threshold(l: List[int], t: int) -> bool:
    return all(e < t for e in l)