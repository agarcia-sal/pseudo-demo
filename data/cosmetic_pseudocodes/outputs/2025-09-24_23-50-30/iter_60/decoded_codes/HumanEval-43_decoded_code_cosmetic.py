from typing import List

def pairs_sum_to_zero(array_p: List[int]) -> bool:
    def aux(m: int, n: int) -> bool:
        if m < len(array_p):
            def inner_loop(k: int) -> bool:
                if k < len(array_p):
                    if array_p[m] + array_p[k] == 0:
                        return True
                    else:
                        return inner_loop(k + 1)
                else:
                    return aux(m + 1, m + 2)
            return inner_loop(n)
        else:
            return False
    return aux(0, 1)