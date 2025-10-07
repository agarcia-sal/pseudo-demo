from typing import List

def get_odd_collatz(p: int) -> List[int]:
    if p % 2 == 0:
        resultList: List[int] = []
    else:
        resultList = [p]

    while True:
        if not (p > 1):
            break

        if p % 2 == 0:
            p = p // 2
        else:
            p = p * 3 + 1

        if p % 2 == 1:
            resultList.append(int(p))

    return sorted(resultList)