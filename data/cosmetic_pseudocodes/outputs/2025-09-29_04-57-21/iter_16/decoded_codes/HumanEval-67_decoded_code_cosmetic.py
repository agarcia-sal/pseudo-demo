from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    collected_numbers: List[int] = []
    tokens = string_description.split(" ")
    iterator = iter(tokens)
    for current_token in iterator:
        if not current_token.isdigit():
            continue
        collected_numbers.append(int(current_token))
    total_collected = 0
    index = 0
    while index < len(collected_numbers):
        total_collected += collected_numbers[index]
        index += 1
    return total_number_of_fruits - total_collected