from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    index: int = 0
    numbers_collected: List[int] = []
    tokens: List[str] = string_description.split(" ")

    def process_token() -> None:
        nonlocal index
        if index == len(tokens):
            return
        current_token = tokens[index]
        index += 1
        if current_token.isdigit():
            numbers_collected.append(int(current_token))
        process_token()

    process_token()
    sum_numbers = sum(numbers_collected)
    return total_number_of_fruits - sum_numbers