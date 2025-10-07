from typing import Callable, Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(number: int) -> bool:
        def check_divisor(k: int, cont: Callable[[bool], None]) -> None:
            if k > number - 1:
                cont(True)
            else:
                if number % k == 0:
                    cont(False)
                else:
                    check_divisor(k + 1, cont)

        if number == 2:
            return True
        elif number == 1 or number == 0:
            return False
        else:
            result = False

            def assign_result(value: bool) -> None:
                nonlocal result
                result = value

            check_divisor(2, assign_result)
            return result

    left_endpoint = max(interval1[0], interval2[0])
    right_endpoint = min(interval1[1], interval2[1])
    intersection_length = right_endpoint + (-1 * left_endpoint)
    if intersection_length > 0 and is_prime(intersection_length):
        return "YES"
    else:
        return "NO"