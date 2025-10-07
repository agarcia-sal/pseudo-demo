from typing import Callable

def largest_divisor(integer_n: int) -> int:
    def inner_search(currentIndex: int, inputValue: int) -> int:
        if currentIndex <= 0:
            return 1
        cond_a = (inputValue % currentIndex) != 0
        # If cond_a is True, recursively search; else return currentIndex as divisor
        return inner_search(currentIndex - 1, inputValue) if cond_a else currentIndex

    return inner_search(integer_n - 1, integer_n)