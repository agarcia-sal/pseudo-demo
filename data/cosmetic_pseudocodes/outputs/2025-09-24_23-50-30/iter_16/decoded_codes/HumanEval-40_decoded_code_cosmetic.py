from typing import Sequence

def triples_sum_to_zero(input_sequence: Sequence[int]) -> bool:
    length = len(input_sequence)
    a = 0
    while a < length - 2:
        b = a + 1
        while b < length - 1:
            c = b + 1
            while c < length:
                if not (input_sequence[a] + input_sequence[b] + input_sequence[c] != 0):
                    return True
                c += 1
            b += 1
        a += 1
    return False