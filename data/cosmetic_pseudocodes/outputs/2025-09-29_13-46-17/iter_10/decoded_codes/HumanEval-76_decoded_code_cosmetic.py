from typing import Union


def is_simple_power(x: int, n: int) -> Union[bool, int]:
    # If n == 1, return whether x != 1
    if n == 1:
        return x != 1

    # Define helper function for integer nth root
    def int_nth_root(value: int, degree: int) -> int:
        # Binary search for the integer nth root of value
        low, high = 1, value
        while low <= high:
            mid = (low + high) // 2
            power = mid ** degree
            if power < value:
                low = mid + 1
            elif power > value:
                high = mid - 1
            else:
                return mid
        return high

    root = int_nth_root(x, n)
    if root ** n == x:
        return root
    else:
        return False