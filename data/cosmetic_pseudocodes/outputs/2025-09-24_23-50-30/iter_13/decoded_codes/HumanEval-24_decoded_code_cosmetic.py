from typing import List

def largest_divisor(integer_n: int) -> int:
    candidate_list: List[int] = []
    for number in range(1, integer_n):
        if integer_n % number == 0:
            candidate_list.append(number)
    return max(candidate_list)