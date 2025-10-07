from typing import List


def fizz_buzz(integer_n: int) -> int:
    def divisible_filter(x: int) -> bool:
        return (x % 11 == 0) or (x % 13 == 0)

    filtered_numbers: List[int] = []
    index_tracker: int = 0
    while index_tracker < integer_n:
        if divisible_filter(index_tracker):
            filtered_numbers.append(index_tracker)
        index_tracker += 1

    combined_text: str = ""
    for value in filtered_numbers:
        combined_text += str(value)

    seven_counter: int = 0
    for symbol in combined_text:
        if symbol == '7':
            seven_counter += 1

    return seven_counter