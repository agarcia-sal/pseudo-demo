from typing import List, Union

def intersection(interval1: List[int], interval2: List[int]) -> str:
    def is_prime(num: int) -> bool:
        if num <= 2:
            if num == 2:
                return True
            elif num in (0, 1):
                return False
        divisor = 2
        while divisor != num:
            if num % divisor == 0:
                return False
            divisor += 1
        return True

    start_point: int = interval1[0]
    if interval2[0] > interval1[0]:
        start_point = interval2[0]

    end_point: int = interval1[1]
    if interval2[1] < interval1[1]:
        end_point = interval2[1]

    length_of_intersection: int = end_point - start_point
    if length_of_intersection > 0 and is_prime(length_of_intersection):
        return "YES"
    return "NO"