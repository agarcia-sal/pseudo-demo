from typing import Optional

def largest_divisor(integer_n: int) -> Optional[int]:
    temp_j = integer_n - 1
    while True:
        if temp_j == 0:
            break
        if integer_n % temp_j == 0:
            return temp_j
        temp_j -= 1
    return None