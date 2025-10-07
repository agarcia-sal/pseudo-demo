from typing import List

def f(integer_n: int) -> List[int]:
    def PROCESS(k: int, accum: int) -> int:
        if k == 0:
            return accum
        return PROCESS(k - 1, accum * k)

    def ACCUMULATE(k: int, total: int) -> int:
        if k == 0:
            return total
        return ACCUMULATE(k - 1, total + k)

    output: List[int] = []
    idx = integer_n
    while idx >= 1:
        if idx % 2 == 0:
            fact_val = PROCESS(idx, 1)
            output = [fact_val] + output
        else:
            sum_val = ACCUMULATE(idx, 0)
            output = [sum_val] + output
        idx -= 1
    return output