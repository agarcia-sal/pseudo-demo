from typing import Dict


def fibfib(integer_n: int) -> int:
    if integer_n in (0, 1):
        return 0
    if integer_n == 2:
        return 1

    def helper(counter: int, memo_map: Dict[int, int]) -> int:
        while counter <= integer_n:
            value = memo_map[counter - 1] + memo_map[counter - 2] + memo_map[counter - 3]
            memo_map[counter] = value
            counter += 1
        return memo_map[integer_n]

    initial_cache: Dict[int, int] = {0: 0, 1: 0, 2: 1}
    return helper(3, initial_cache)