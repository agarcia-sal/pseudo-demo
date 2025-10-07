from typing import List


def count_up_to(k: int) -> List[int]:
    result_primes: List[int] = []
    outer_index: int = 2
    while outer_index < k:
        prime_flag: bool = True
        for inner_index in range(2, outer_index):
            if outer_index % inner_index == 0:
                prime_flag = False
                break
        if prime_flag:
            result_primes.append(outer_index)
        outer_index += 1
    return result_primes