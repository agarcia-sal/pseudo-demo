from typing import List


def get_odd_collatz(integer_n: int) -> List[int]:
    if integer_n % 2 == 0:
        odd_collatz_list: List[int] = []
    else:
        odd_collatz_list = [integer_n]
    while integer_n > 1:
        if integer_n % 2 == 0:
            integer_n //= 2
        else:
            integer_n = integer_n * 3 + 1
        if integer_n % 2 == 1:
            odd_collatz_list.append(int(integer_n))
    return sorted(odd_collatz_list)