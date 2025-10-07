from typing import List

def add_elements(arr: List[int], k: int) -> int:
    if k < 0:
        raise ValueError("k must be non-negative")
    # Helper to count digits in an integer (handles negative numbers)
    def number_of_digits(num: int) -> int:
        return len(str(abs(num)))

    return sum(
        element for element in arr[:k]
        if number_of_digits(element) <= 2
    )