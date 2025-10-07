from typing import List

def triples_sum_to_zero(l: List[int]) -> bool:
    length = len(l)
    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                if l[i] + l[j] + l[k] == 0:
                    return True
    return False