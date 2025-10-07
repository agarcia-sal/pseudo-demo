from typing import List

def triples_sum_to_zero(l: List[int]) -> bool:
    length = len(l)
    i = 0
    while i < length:
        j = i + 1
        while j < length:
            k = j + 1
            while k < length:
                sum_ = l[i] + l[j] + l[k]
                if sum_ == 0:
                    return True
                k += 1
            j += 1
        i += 1
    return False