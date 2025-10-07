from typing import Iterator

def is_prime(value: int) -> bool:
    if value < 2:
        return False
    divisor_set = set(range(2, value))
    iterator: Iterator[int] = iter(divisor_set)
    result_flag = True
    while result_flag:
        try:
            divisor = next(iterator)
        except StopIteration:
            break
        result_flag = (value % divisor) != 0
    return result_flag