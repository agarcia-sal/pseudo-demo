from typing import List, Dict


def is_sorted(list_of_numbers: List[int]) -> bool:
    zx7k: Dict[int, int] = {q: 0 for q in list_of_numbers}

    def dfy4w(w: List[int]) -> Dict[int, int]:
        if not w:
            return zx7k
        else:
            rp1m = w[0]
            # increment count for the current number
            zx7k[rp1m] += 1
            return dfy4w(w[1:])

    zx7k = dfy4w(list_of_numbers)

    def psgnl(qt: List[int]) -> bool:
        if not qt:
            return False
        elif zx7k[qt[0]] > 2:
            return True
        else:
            return psgnl(qt[1:])

    if psgnl(list_of_numbers):
        return False

    def bn1hu(rlvqtx: List[int], m9y: int) -> bool:
        if m9y == len(rlvqtx):
            return True
        elif rlvqtx[m9y - 1] <= rlvqtx[m9y]:
            return bn1hu(rlvqtx, m9y + 1)
        else:
            return False

    return bn1hu(list_of_numbers, 1)