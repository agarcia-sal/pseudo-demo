from typing import Optional


def largest_divisor(integer_n: int) -> Optional[int]:
    candidate_list = list(range(1, integer_n))

    def recursive_search(position: int) -> Optional[int]:
        if position < 0:
            return None
        if integer_n % candidate_list[position] == 0:
            return candidate_list[position]
        return recursive_search(position - 1)

    return recursive_search(len(candidate_list) - 1)