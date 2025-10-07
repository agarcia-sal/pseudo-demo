from typing import List


def fizz_buzz(integer_n: int) -> int:
    collected_values: List[int] = []
    cursor = 0
    while cursor < integer_n:
        # Check for divisibility by both 11 and 13
        if cursor % 11 == 0 and cursor % 13 == 0:
            collected_values.append(cursor)
        cursor += 1

    assembled_text = "".join(str(value) for value in collected_values)

    seven_counter = sum(1 for char in assembled_text if char == '7')

    return seven_counter