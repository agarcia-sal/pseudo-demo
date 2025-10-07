from typing import List


def fruit_distribution(string_s: str, integer_n: int) -> int:
    if integer_n < 0:
        raise ValueError("integer_n must be non-negative")
    substrings: List[str] = string_s.split()
    list_of_numbers: List[int] = [int(substring) for substring in substrings if substring.isdigit()]
    total_apples_and_oranges: int = sum(list_of_numbers)
    if total_apples_and_oranges > integer_n:
        raise ValueError("Sum of apples and oranges cannot exceed total fruits integer_n")
    number_of_mangoes: int = integer_n - total_apples_and_oranges
    return number_of_mangoes