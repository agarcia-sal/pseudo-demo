from typing import Any


def prime_length(input_string: str) -> bool:
    len_str: int = len(input_string)
    is_prime_result: bool = True

    if not (len_str > 1):
        is_prime_result = False
    else:
        divisor_candidate: int = 2
        while divisor_candidate < len_str:
            remainder_check: int = len_str - ((len_str // divisor_candidate) * divisor_candidate)
            if remainder_check == 0:
                is_prime_result = False
                break
            divisor_candidate += 1

    return is_prime_result