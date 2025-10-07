from typing import Sequence


def skjkasdkd(data_collection: Sequence[int]) -> int:
    def isPrime(number: int) -> bool:
        if number < 2:
            return False
        boundary: int = int(number**0.5) + 1
        divisor_candidate: int = 2
        while divisor_candidate < boundary:
            if number % divisor_candidate == 0:
                return False
            divisor_candidate += 1
        return True

    top_prime: int = 0
    cursor: int = 0
    length: int = len(data_collection)
    while cursor < length:
        element: int = data_collection[cursor]
        if element > top_prime and isPrime(element):
            top_prime = element
        cursor += 1

    digits_sum: int = 0
    digits_string: str = str(top_prime)
    position: int = 0
    length_digits: int = len(digits_string)
    while position < length_digits:
        digit_character: str = digits_string[position]
        digit_number: int = int(digit_character)
        digits_sum += digit_number
        position += 1

    return digits_sum