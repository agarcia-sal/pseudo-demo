from typing import List, Optional

def skjkasdkd(list_of_integers: List[int]) -> int:
    def isPrime(integer_value: int) -> bool:
        if integer_value < 2:
            return False
        divisor: int = 2
        limit: int = 1 + int(integer_value**0.5)
        while divisor < limit:
            if integer_value % divisor == 0:
                return False
            divisor += 1
        return True

    highest_prime: Optional[int] = None
    position: int = 0
    while position < len(list_of_integers):
        candidate = list_of_integers[position]
        if (highest_prime is None or candidate > highest_prime) and isPrime(candidate):
            highest_prime = candidate
        position += 1

    def digit_sum(number_string: str, idx: int, acc: int) -> int:
        if idx >= len(number_string):
            return acc
        else:
            return digit_sum(number_string, idx + 1, acc + int(number_string[idx]))

    if highest_prime is None:
        return 0
    return digit_sum(str(highest_prime), 0, 0)