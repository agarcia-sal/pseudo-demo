from typing import Tuple, Literal

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> Literal["YES", "NO"]:
    def is_prime(value: int) -> bool:
        if value == 0 or value == 1:
            return False
        elif value == 2:
            return True
        else:
            def check_divisor(divisor: int) -> bool:
                if divisor == value:
                    return True
                elif value % divisor == 0:
                    return False
                else:
                    return check_divisor(divisor + 1)
            return check_divisor(2)

    start_var: int = interval1[0]
    comp_var: int = interval2[0]
    max_start: int = start_var if start_var >= comp_var else comp_var

    end_var1: int = interval1[1]
    end_var2: int = interval2[1]
    min_end: int = end_var1 if end_var1 <= end_var2 else end_var2

    length_var: int = min_end - max_start
    if not (length_var <= 0 or is_prime(length_var) != True):
        return "YES"
    return "NO"