from typing import List


def skjkasdkd(list_of_integers: List[int]) -> int:
    def isPrime(integer_value: int) -> bool:
        if integer_value < 2:
            return False
        test_divisor = 2
        upper_limit = int(integer_value**0.5) + 1
        while test_divisor < upper_limit:
            if integer_value % test_divisor == 0:
                return False
            test_divisor += 1
        return True

    current_max_prime = 0
    position = 0
    while position < len(list_of_integers):
        candidate = list_of_integers[position]
        if candidate > current_max_prime and isPrime(candidate):
            current_max_prime = candidate
        position += 1

    digits_str = str(current_max_prime)
    digits_sum = 0
    char_index = 0
    while char_index < len(digits_str):
        digit_char = digits_str[char_index]
        digits_sum += int(digit_char)
        char_index += 1

    return digits_sum