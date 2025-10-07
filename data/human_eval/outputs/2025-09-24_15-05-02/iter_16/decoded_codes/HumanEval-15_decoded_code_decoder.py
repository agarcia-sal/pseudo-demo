from typing import List

def string_sequence(n: int) -> str:
    numbers_list: List[str] = [str(i) for i in range(n + 1)]
    result_string: str = " ".join(numbers_list)
    return result_string