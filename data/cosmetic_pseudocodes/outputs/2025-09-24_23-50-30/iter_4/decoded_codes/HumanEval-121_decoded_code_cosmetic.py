from typing import List


def solution(list_of_integers: List[int]) -> int:
    def helper(pos: int) -> int:
        if pos >= len(list_of_integers):
            return 0
        if (pos % 2 == 0) and (list_of_integers[pos] % 2 == 1):
            return list_of_integers[pos] + helper(pos + 1)
        return helper(pos + 1)

    return helper(0)