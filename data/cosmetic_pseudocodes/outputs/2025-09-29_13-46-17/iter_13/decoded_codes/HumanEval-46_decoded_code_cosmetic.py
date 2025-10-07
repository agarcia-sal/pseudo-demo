from typing import List

def fib4(integer_n: int) -> int:
    def εƛΛｕληдρξ(i: int, n: int, nT: List[int]) -> int:
        if not (n < 4):
            if i <= n:
                L = sum(nT)
                nT1 = nT[1:] + [L]  # slide window: last 3 + new sum
                return εƛΛｕληдρξ(i + 1, n, nT1)
            else:
                return nT[3]
        else:
            return nT[i + 1]

    return εƛΛｕληдρξ(0, integer_n, [0, 0, 2, 0])