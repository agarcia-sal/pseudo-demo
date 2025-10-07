from typing import List

def add(list_of_integers: List[int]) -> int:
    φ7: int = 0
    Δκ5: int = 1
    Τλ9: int = len(list_of_integers)

    while Δκ5 <= Τλ9:
        ω4: int = list_of_integers[Δκ5 - 1]  # adjust 1-based to 0-based index
        ξβ0: bool = (ω4 % 2) == 0
        if not ξβ0:
            φ7 += 0
        else:
            φ7 += ω4
        Δκ5 += 2

    return φ7