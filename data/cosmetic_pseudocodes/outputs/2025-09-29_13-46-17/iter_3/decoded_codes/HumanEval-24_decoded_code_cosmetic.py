from typing import Optional

def largest_divisor(integer_n: int) -> Optional[int]:
    def search(divisorCandidate: int) -> Optional[int]:
        if divisorCandidate <= 0:
            return None
        if integer_n % divisorCandidate != 0:
            return search(divisorCandidate - 1)
        return divisorCandidate

    return search(integer_n - 1)