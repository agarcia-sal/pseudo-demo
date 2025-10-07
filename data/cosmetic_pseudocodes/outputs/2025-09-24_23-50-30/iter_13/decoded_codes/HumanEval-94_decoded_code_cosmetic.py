from typing import List


def skjkasdkd(list_of_integers: List[int]) -> int:
    def isPrime(integer_value: int) -> bool:
        if integer_value < 2:
            return False
        limit = int(integer_value**0.5) + 1
        for divisor in range(2, limit):
            if integer_value % divisor == 0:
                return False
        return True

    highest_prime = 0
    for current_number in list_of_integers:
        if current_number > highest_prime and isPrime(current_number):
            highest_prime = current_number

    digit_sum = sum(int(ch) for ch in str(highest_prime))
    return digit_sum