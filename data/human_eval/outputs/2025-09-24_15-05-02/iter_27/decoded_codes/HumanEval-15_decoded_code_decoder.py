from typing import List

def string_sequence(n: int) -> str:
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    list_of_strings: List[str] = [str(x) for x in range(n + 1)]
    result_string: str = " ".join(list_of_strings)
    return result_string