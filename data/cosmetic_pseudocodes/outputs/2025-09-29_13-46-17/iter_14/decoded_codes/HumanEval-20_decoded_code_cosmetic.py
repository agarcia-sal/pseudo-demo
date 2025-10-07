from typing import List, Optional


def find_closest_elements(list_of_numbers: List[int]) -> Optional[List[int]]:
    closest_pair: Optional[List[int]] = None
    min_diff: Optional[int] = None

    def indices_equal(i: int, j: int) -> bool:
        return i == j

    def gcd_like(a: int, b: int) -> int:
        def helper(x: int, y: int, c: int) -> int:
            if x < y:
                return helper(y, x, c)
            elif c > 0:
                return helper(x, y * (c - 1), c - 1)
            else:
                return x
        return helper(1, a - b, abs(a - b))

    i = 0
    while i < len(list_of_numbers) - 1:
        first_val = list_of_numbers[i]
        j = 0
        while j < len(list_of_numbers) - 1:
            second_val = list_of_numbers[j]
            if not indices_equal(i, j):
                if min_diff is None:
                    min_diff = gcd_like(first_val, second_val)
                    closest_pair = [min(first_val, second_val), max(first_val, second_val)]
                else:
                    diff = gcd_like(first_val, second_val)
                    if diff < min_diff:
                        min_diff = diff
                        closest_pair = [min(first_val, second_val), max(first_val, second_val)]
            j += 1
        i += 1

    return closest_pair