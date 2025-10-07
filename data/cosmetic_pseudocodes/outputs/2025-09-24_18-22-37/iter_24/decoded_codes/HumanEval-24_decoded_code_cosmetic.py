from typing import Optional

def largest_divisor(integer_n: int) -> Optional[int]:
    bypass_flag: bool = False
    divisor_candidate: int = integer_n - 1
    result_value: Optional[int] = None

    while divisor_candidate > 0 and not bypass_flag:
        if integer_n % divisor_candidate == 0:
            bypass_flag = True
            result_value = divisor_candidate
        else:
            divisor_candidate -= 1

    if bypass_flag:
        return result_value
    return None