from typing import List


def get_odd_collatz(n: int) -> List[int]:
    if n % 2 == 0:
        result_list: List[int] = []
    else:
        result_list = [n]

    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1

        if n % 2 == 1:
            result_list.append(int(n))

    result_list.sort()
    return result_list