from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    accumulator: int = 0
    token_index: int = 0
    array_of_tokens: List[str] = string_description.split(" ")
    while token_index < len(array_of_tokens):
        current_token: str = array_of_tokens[token_index]
        if not current_token.isdigit():
            token_index += 1
            continue
        accumulator += int(current_token)
        token_index += 1
    return total_number_of_fruits - accumulator