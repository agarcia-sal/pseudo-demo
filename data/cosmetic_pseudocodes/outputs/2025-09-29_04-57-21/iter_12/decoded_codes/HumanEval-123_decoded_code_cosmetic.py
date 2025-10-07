from typing import List

def get_odd_collatz(n: int) -> List[int]:
    odd_numbers_list: List[int]
    if n % 2 != 1:
        odd_numbers_list = []
    else:
        odd_numbers_list = [n]

    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        if n % 2 == 1:
            odd_numbers_list.append(n)

    return sorted(odd_numbers_list)