from typing import List

def count_up_to(m: int) -> List[int]:
    prime_numbers: List[int] = []
    k: int = 2

    while k < m:
        verdict: bool = True
        divisor: int = 2

        while divisor < k and verdict:
            if k % divisor == 0:
                verdict = False
            else:
                divisor += 1

        if verdict:
            prime_numbers.append(k)

        k += 1

    return prime_numbers