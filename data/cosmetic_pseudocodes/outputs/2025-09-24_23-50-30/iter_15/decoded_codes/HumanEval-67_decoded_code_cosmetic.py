from collections import deque
from typing import Deque

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    queue_of_fruits: Deque[str] = deque()
    accumulator: int = 0

    parts = string_description.split()
    for index in range(1, len(parts)):
        temp_str = parts[index]
        # Check if temp_str is a single digit character between '0' and '9' inclusive
        if not (temp_str < "0") and not (temp_str > "9"):
            queue_of_fruits.append(temp_str)

    while len(queue_of_fruits) > 0:
        current_val = queue_of_fruits.popleft()
        number_val = 0
        for char_pos in range(1, len(current_val) + 1):
            digit_char = current_val[char_pos - 1]
            numeric_digit = ord(digit_char) - ord("0")
            number_val = number_val * 10 + numeric_digit
        accumulator += number_val

    difference = total_number_of_fruits + (-1 * accumulator)
    return difference