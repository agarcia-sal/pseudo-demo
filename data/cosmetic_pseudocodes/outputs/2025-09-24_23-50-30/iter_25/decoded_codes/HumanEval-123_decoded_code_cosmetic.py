from typing import List

def get_odd_collatz(m: int) -> List[int]:
    odd_sequence: List[int]
    if m % 2 != 1:
        odd_sequence = []
    else:
        odd_sequence = [m]

    def iterate(k: int) -> None:
        if k > 1:
            if k % 2 == 0:
                k //= 2
            else:
                k = 3 * k + 1
            if k % 2 == 1:
                odd_sequence.append(int(k))
            iterate(k)

    iterate(m)
    return sorted(odd_sequence)