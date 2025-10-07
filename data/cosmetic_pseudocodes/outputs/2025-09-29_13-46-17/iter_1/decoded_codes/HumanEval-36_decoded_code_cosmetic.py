from typing import List


def fizz_buzz(integer_n: int) -> int:
    collected_numbers: List[int] = [i for i in range(integer_n) if i % 11 == 0 or i % 13 == 0]
    combined_string: str = "".join(str(num) for num in collected_numbers)
    sevens_counter: int = sum(1 for char in combined_string if char == '7')
    return sevens_counter