from typing import List

def fruit_distribution(string_s: str, integer_n: int) -> int:
    numeric_values: List[int] = []
    for word in string_s.split():
        if word.isdigit():
            numeric_values.append(int(word))
    total_apples_and_oranges = sum(numeric_values)
    return integer_n - total_apples_and_oranges