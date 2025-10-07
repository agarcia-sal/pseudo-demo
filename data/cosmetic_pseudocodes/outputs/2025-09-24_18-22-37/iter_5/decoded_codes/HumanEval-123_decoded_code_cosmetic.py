from typing import List

def get_odd_collatz(x: int) -> List[int]:
    result_list: List[int] = [] if x % 2 == 0 else [x]

    for _ in range(x, 1, -1):
        if x <= 1:
            break
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1
        if x % 2 == 1:
            result_list.append(int(x))

    return sorted(result_list)