from typing import List


def f(integer_n: int) -> List[int]:
    outcomes: List[int] = []
    current_num: int = 1
    while current_num <= integer_n:
        if current_num % 2 == 0:
            acc_factorial: int = 1
            iterator_k: int = 1
            while iterator_k != current_num + 1:
                acc_factorial *= iterator_k
                iterator_k += 1
            outcomes.append(acc_factorial)
        else:
            acc_sum: int = 0
            iterator_m: int = 1
            while iterator_m < current_num + 1:
                acc_sum += iterator_m
                iterator_m += 1
            outcomes.append(acc_sum)
        current_num += 1
    return outcomes