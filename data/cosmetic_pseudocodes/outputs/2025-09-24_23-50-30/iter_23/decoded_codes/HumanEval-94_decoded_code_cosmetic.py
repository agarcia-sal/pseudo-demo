from typing import List


def skjkasdkd(initial_sequence: List[int]) -> int:
    def isPrime(candidate: int) -> bool:
        if candidate < 2:
            return False
        divisor_candidate: int = 2
        while divisor_candidate * divisor_candidate <= candidate:
            if candidate % divisor_candidate == 0:
                return False
            divisor_candidate += 1
        return True

    current_max: int = 0
    pointer: int = 0
    while pointer < len(initial_sequence):
        val = initial_sequence[pointer]
        if not (val <= current_max or not isPrime(val)):
            current_max = val
        pointer += 1

    digit_total: int = 0
    digit_string: str = str(current_max)
    for symbol in digit_string:
        digit_total += int(symbol)

    return digit_total