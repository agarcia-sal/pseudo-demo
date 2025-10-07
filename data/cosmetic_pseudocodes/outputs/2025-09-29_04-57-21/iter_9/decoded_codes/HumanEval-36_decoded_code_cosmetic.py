from typing import List

def fizz_buzz(integer_n: int) -> int:
    collected_values: List[int] = []

    current_val = 0
    while current_val < integer_n:
        if not (current_val % 11 != 0 and current_val % 13 != 0):
            collected_values.append(current_val)
        current_val += 1

    combined_text: str = "".join(str(element) for element in collected_values)

    total_seven_chars: int = sum(1 for each_char in combined_text if each_char == '7')

    return total_seven_chars