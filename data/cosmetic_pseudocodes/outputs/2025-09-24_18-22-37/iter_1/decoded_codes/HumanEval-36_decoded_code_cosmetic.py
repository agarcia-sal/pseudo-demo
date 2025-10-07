from typing import List


def fizz_buzz(integer_n: int) -> int:
    filtered_numbers: List[int] = [index for index in range(integer_n) if index % 11 == 0 or index % 13 == 0]
    combined_str: str = "".join(str(value) for value in filtered_numbers)
    seven_counter: int = sum(1 for char in combined_str if char == '7')
    return seven_counter