from typing import List


def get_odd_collatz(n: int) -> List[int]:
    sequenceList: List[int]
    if n % 2 != 1:
        sequenceList = []
    else:
        sequenceList = [n]

    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        if n & 1 == 1:
            sequenceList.append(int(n))

    return sorted(sequenceList)