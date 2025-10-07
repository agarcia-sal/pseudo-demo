from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    gathered_numbers: List[int] = []
    tokens: List[str] = string_description.split(" ")
    idx: int = 0
    while idx < len(tokens):
        current_token: str = tokens[idx]
        if current_token.isdigit():
            parsed_num: int = int(current_token)
            gathered_numbers.append(parsed_num)
        idx += 1
    total_found: int = 0
    counter: int = 0
    while counter < len(gathered_numbers):
        total_found += gathered_numbers[counter]
        counter += 1
    return total_number_of_fruits - total_found