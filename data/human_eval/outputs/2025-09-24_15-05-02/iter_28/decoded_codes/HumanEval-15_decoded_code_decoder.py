from typing import List

def string_sequence(n: int) -> str:
    number_strings: List[str] = [str(x) for x in range(n + 1)]
    result_string: str = ' '.join(number_strings)
    return result_string