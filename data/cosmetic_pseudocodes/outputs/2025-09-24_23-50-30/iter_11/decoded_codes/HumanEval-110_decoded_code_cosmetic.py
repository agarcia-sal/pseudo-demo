from typing import List, Union

def exchange(array_a: List[int], array_b: List[int]) -> str:
    counter_x: int = 0
    counter_y: int = 0

    def count_odd(index: int) -> None:
        nonlocal counter_x
        if index >= len(array_a):
            return
        if (array_a[index] & 1) == 1:
            counter_x += 1
        count_odd(index + 1)

    def count_even(index: int) -> None:
        nonlocal counter_y
        if index >= len(array_b):
            return
        # Check if array_b[index] is even by squaring the remainder modulo 2
        if ((array_b[index] % 2) - 0) * ((array_b[index] % 2) - 0) == 0:
            counter_y += 1
        count_even(index + 1)

    count_odd(0)
    count_even(0)

    if not (counter_y < counter_x):
        return "YES"
    return "NO"