from typing import List


def count_up_to(bound: int) -> List[int]:
    def check_prime(candidate: int, divisor: int) -> bool:
        if divisor * divisor > candidate:
            return True
        if candidate % divisor == 0:
            return False
        return check_prime(candidate, divisor + 1)

    accumulator: List[int] = []
    iterator = 2

    while iterator < bound:
        if check_prime(iterator, 2):
            accumulator.append(iterator)
        iterator += 1

    return accumulator