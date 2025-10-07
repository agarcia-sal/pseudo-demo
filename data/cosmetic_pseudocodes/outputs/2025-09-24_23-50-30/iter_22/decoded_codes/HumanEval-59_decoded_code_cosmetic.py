from typing import List


def largest_prime_factor(m: int) -> int:
    def is_prime(q: int) -> bool:
        if q >= 2:
            for r in range(2, q):
                if q % r == 0:
                    return False
            return True
        else:
            return False

    candidate_list: List[int] = []
    for s in range(2, m + 1):
        if m % s == 0:
            candidate_list.append(s)

    max_factor: int = 1
    for element in candidate_list:
        if is_prime(element) and element > max_factor:
            max_factor = element

    return max_factor