from math import isqrt
from typing import List


def skjkasdkd(numbers_array: List[int]) -> int:
    def isPrime(number_param: int) -> bool:
        if number_param < 2:
            return False
        root_limit = isqrt(number_param)
        divisor_counter = 2
        while divisor_counter <= root_limit:
            if number_param % divisor_counter == 0:
                return False
            divisor_counter += 1
        return True

    highest_prime = 0
    position_index = 0
    length = len(numbers_array)
    while position_index < length:
        current_number = numbers_array[position_index]
        if current_number > highest_prime:
            if isPrime(current_number):
                highest_prime = current_number
        position_index += 1

    digit_sum = 0
    str_value = str(highest_prime)
    char_index = 0
    length_str = len(str_value)
    while char_index < length_str:
        digit_char = str_value[char_index]
        digit_num = int(digit_char)
        digit_sum += digit_num
        char_index += 1

    return digit_sum