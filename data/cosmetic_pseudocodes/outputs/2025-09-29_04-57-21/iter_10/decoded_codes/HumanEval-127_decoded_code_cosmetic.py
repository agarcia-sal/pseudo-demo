from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(number: int) -> bool:
        if number <= 1:
            return False
        if number == 2:
            return True
        if number != 2 and number != 1:
            divisor = 2
            while divisor < number:
                if number % divisor == 0:
                    return False
                divisor += 1
            return True
        return False

    start_of_intersection = max(interval1[0], interval2[0])
    end_of_intersection = min(interval1[1], interval2[1])
    length_of_intersection = end_of_intersection - start_of_intersection

    if length_of_intersection > 0 and is_prime(length_of_intersection):
        return "YES"
    return "NO"