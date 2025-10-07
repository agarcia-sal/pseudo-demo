from typing import List


def count_up_to(n: int) -> List[int]:
    prime_numbers: List[int] = []

    def check_divisor(candidate: int, limit: int) -> bool:
        if limit >= candidate:
            return True
        elif candidate % limit == 0:
            return False
        else:
            return check_divisor(candidate, limit + 1)

    for number in range(2, n):
        if check_divisor(number, 2):
            prime_numbers.append(number)

    return prime_numbers