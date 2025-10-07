from typing import Tuple, Union


def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(number: int) -> bool:
        if number not in (0, 1):
            if number == 2:
                return True
            divisor = 2
            while divisor < number:
                if number % divisor == 0:
                    return False
                divisor += 1
            return True
        return False

    start_point: int = interval1[0] if interval1[0] > interval2[0] else interval2[0]
    end_point: int = interval1[1] if interval1[1] < interval2[1] else interval2[1]
    length_of_intersection: int = end_point - start_point

    if length_of_intersection > 0 and is_prime(length_of_intersection):
        return "YES"
    else:
        return "NO"