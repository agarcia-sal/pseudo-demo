from typing import Optional

def largest_divisor(integer_n: int) -> Optional[int]:
    if integer_n <= 1:
        return None  # No divisors less than n for 0 or 1
    index_k: int = integer_n - 1
    while index_k > 0:
        if integer_n % index_k == 0:
            return index_k
        index_k -= 1
    return None  # fallback, though for n > 1 this won't happen