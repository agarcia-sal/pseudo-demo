from typing import List


def count_up_to(q: int) -> List[int]:
    found_primes: List[int] = []
    outer_idx: int = 2
    while outer_idx < q:
        prime_flag: bool = True
        inner_idx: int = 2
        while inner_idx < outer_idx:
            remainder: int = outer_idx % inner_idx
            if remainder == 0:
                prime_flag = False
                break
            inner_idx += 1
        if prime_flag:
            found_primes.append(outer_idx)
        outer_idx += 1
    return found_primes