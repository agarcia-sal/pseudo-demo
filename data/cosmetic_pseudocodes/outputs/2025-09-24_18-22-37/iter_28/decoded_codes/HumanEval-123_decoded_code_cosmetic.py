from typing import List

def get_odd_collatz(q: int) -> List[int]:
    if q % 2 == 0:
        result_sequence: List[int] = []
    else:
        result_sequence = [q]

    while q > 1:
        if q % 2 == 0:
            q = q // 2
        else:
            q = q * 3 + 1

        if q % 2 == 1:
            result_sequence.append(q)

    return sorted(result_sequence)