from typing import List

def f(count: int) -> List[int]:
    output: List[int] = []
    current: int = 1

    while current <= count:
        temp: int = 1
        if current % 2 == 0:
            k: int = 1
            while k <= current:
                temp *= k
                k += 1
        else:
            total: int = 0
            idx: int = 1
            while idx <= current:
                total += idx
                idx += 1
            temp = total
        output.append(temp)
        current += 1

    return output