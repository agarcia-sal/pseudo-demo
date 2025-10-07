from typing import Union

def is_prime(number: Union[int, float]) -> bool:
    if not isinstance(number, int) or number < 2:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True