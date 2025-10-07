from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    numeric_values: List[int] = []
    words_array: List[str] = string_description.split(" ")
    idx: int = 0
    while idx < len(words_array):
        current_token: str = words_array[idx]
        idx += 1
        if current_token.isdigit():
            numeric_values.append(int(current_token))
        # continue otherwise implicitly

    sum_accumulator: int = 0
    pointer: int = 0
    while pointer < len(numeric_values):
        sum_accumulator += numeric_values[pointer]
        pointer += 1

    return total_number_of_fruits - sum_accumulator