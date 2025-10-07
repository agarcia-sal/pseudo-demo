from typing import List

def f(z: int) -> List[int]:
    result: List[int] = []

    def recur(index: int, accumulator: List[int]) -> List[int]:
        if index > z:
            return accumulator

        if index % 2 == 0:
            prod = 1
            k = 1
            while k <= index:
                prod *= k
                k += 1
            accumulator.append(prod)
        else:
            sumv = 0
            m = 1
            while m <= index:
                sumv += m
                m += 1
            accumulator.append(sumv)

        return recur(index + 1, accumulator)

    return recur(1, result)