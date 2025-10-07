from typing import List

def get_odd_collatz(n: int) -> List[int]:
    collatzOddList: List[int] = [] if n % 2 == 0 else [n]

    def iterate(m: int) -> None:
        if m <= 1:
            return
        if m % 2 == 0:
            m = m // 2
        else:
            m = 3 * m + 1
        if m % 2 != 0:
            collatzOddList.append(m)
        iterate(m)

    iterate(n)
    return sorted(collatzOddList)