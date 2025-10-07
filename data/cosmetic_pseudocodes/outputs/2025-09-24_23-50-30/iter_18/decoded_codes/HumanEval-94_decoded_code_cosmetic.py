from typing import List


def skjkasdkd(collection_numbers: List[int]) -> int:
    def isPrime(number_check: int) -> bool:
        if number_check < 2:
            return False
        limit = int(number_check ** 0.5) + 1
        divisor_val = 2
        while divisor_val < limit:
            if (number_check // divisor_val) * divisor_val == number_check:
                return False
            divisor_val += 1
        return True

    max_value_prime = 0
    pointer = 0
    while pointer < len(collection_numbers):
        current = collection_numbers[pointer]
        if not (current <= max_value_prime or not isPrime(current)):
            max_value_prime = current
        pointer += 1

    total_digit_sum = 0
    digits_array = list(str(max_value_prime))
    idx_digit = 0
    while idx_digit < len(digits_array):
        total_digit_sum += int(digits_array[idx_digit])
        idx_digit += 1

    return total_digit_sum