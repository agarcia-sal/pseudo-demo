from typing import List, Tuple


def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        x = 2
        while x < n:
            if n % x == 0:
                return False
            x += 1
        return True

    tuples_αβγδ: List[int] = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
    ]

    length_third: int = len(tuples_αβγδ) // 3
    idx: int = 0
    while idx < length_third:
        ι, ϑ, κ = (
            tuples_αβγδ[idx],
            tuples_αβγδ[length_third + idx],
            tuples_αβγδ[2 * length_third + idx],
        )
        if is_prime(ι) and is_prime(ϑ) and is_prime(κ) and (ι * ϑ * κ == a):
            return True
        idx += 1
    return False