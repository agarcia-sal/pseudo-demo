from typing import List

def get_odd_collatz(n: int) -> List[int]:
    def recurseCollatz(current: int, acc: List[int]) -> List[int]:
        if current == 1:
            return acc

        if current % 2 != 0:
            nextVal = current * 3 + 1
        else:
            nextVal = current // 2  # use integer division

        if nextVal % 2 != 0:
            return recurseCollatz(nextVal, acc + [int(nextVal)])
        else:
            return recurseCollatz(nextVal, acc)

    initialAcc = [n] if n % 2 != 0 else []
    resultList = recurseCollatz(n, initialAcc)
    return sorted(resultList)