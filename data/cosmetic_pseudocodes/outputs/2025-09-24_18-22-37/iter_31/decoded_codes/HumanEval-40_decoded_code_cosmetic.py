from typing import List


def triples_sum_to_zero(array_numbers: List[int]) -> bool:
    length = len(array_numbers)
    pos = 0
    while pos < length:
        next_pos = pos + 1
        while next_pos < length:
            last_pos = next_pos + 1
            while last_pos < length:
                val1 = array_numbers[pos]
                val2 = array_numbers[next_pos]
                val3 = array_numbers[last_pos]
                total_sum = val1 + val2 + val3
                if total_sum == 0:
                    return True
                last_pos += 1
            next_pos += 1
        pos += 1
    return False