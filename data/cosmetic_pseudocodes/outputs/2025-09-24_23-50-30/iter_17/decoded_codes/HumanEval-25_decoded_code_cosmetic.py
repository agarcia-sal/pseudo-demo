from typing import List, Set

def factorize(input_num: int) -> List[int]:
    output_set: Set[int] = set()
    current_divisor = 2
    max_limit = int(input_num**0.5) + 1
    for current_divisor in range(2, max_limit + 1):
        while input_num % current_divisor == 0:
            output_set.add(current_divisor)
            input_num //= current_divisor
    if input_num > 1:
        output_set.add(input_num)
    return list(output_set)