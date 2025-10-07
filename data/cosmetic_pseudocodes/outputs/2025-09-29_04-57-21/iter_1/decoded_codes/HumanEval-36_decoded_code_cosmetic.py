from typing import List


def fizz_buzz(integer_n: int) -> int:
    multiples: List[int] = [counter for counter in range(integer_n) if counter % 11 == 0 or counter % 13 == 0]

    combined_str: str = "".join(str(element) for element in multiples)

    sevens_count: int = sum(ch == '7' for ch in combined_str)

    return sevens_count