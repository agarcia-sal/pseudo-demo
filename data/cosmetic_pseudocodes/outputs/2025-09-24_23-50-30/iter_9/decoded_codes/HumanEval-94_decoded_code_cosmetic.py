from typing import Sequence

def skjkasdkd(opaque_collection: Sequence[int]) -> int:
    def isPrime(num: int) -> bool:
        if num < 2:
            return False
        threshold = int(num**0.5) + 1
        factor = 2
        while factor < threshold:
            if num % factor == 0:
                return False
            factor += 1
        return True

    largest_prime = 0
    cursor = 0
    length = len(opaque_collection)
    while cursor < length:
        val = opaque_collection[cursor]
        if not (val <= largest_prime or not isPrime(val)):
            largest_prime = val
        cursor += 1

    digit_sum = sum(int(d) for d in str(largest_prime))
    return digit_sum