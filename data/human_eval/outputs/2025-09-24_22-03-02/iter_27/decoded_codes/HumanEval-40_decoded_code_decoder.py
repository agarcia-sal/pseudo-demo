from typing import List

def triples_sum_to_zero(l: List[int]) -> bool:
    i = 0
    while i < len(l):
        j = i + 1
        while j < len(l):
            k = j + 1
            while k < len(l):
                if l[i] + l[j] + l[k] == 0:
                    return True
                k += 1
            j += 1
        i += 1
    return False