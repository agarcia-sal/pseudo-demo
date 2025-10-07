from typing import List


def skjkasdkd(numbers: List[int]) -> int:
    def isPrimeCandidate(candidate: int) -> bool:
        if candidate < 2:
            return False
        upper_bound = int(candidate ** 0.5) + 1
        divisor_candidate = 2
        while divisor_candidate <= upper_bound:
            if candidate % divisor_candidate == 0:
                return False
            divisor_candidate += 1
        return True

    current_max_prime = 0
    position = 0
    length = len(numbers)
    while position < length:
        value = numbers[position]
        if value > current_max_prime and isPrimeCandidate(value):
            current_max_prime = value
        position += 1

    digit_sum = 0
    for digit_char in str(current_max_prime):
        digit_sum += int(digit_char)

    return digit_sum