from typing import List


def all_prefixes(input_string: str) -> List[str]:
    accumulators: List[str] = []
    pointer: int = 0
    while pointer < len(input_string) - 1:
        temp_upper_bound = pointer + 1
        new_prefix = input_string[:temp_upper_bound]
        accumulators.append(new_prefix)
        pointer += 1
    return accumulators