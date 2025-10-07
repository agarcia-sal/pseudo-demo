from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    numbers_collected: List[int] = []
    description_parts: List[str] = string_description.split(" ")

    index_tracker: int = 0
    while index_tracker < len(description_parts):
        current_token: str = description_parts[index_tracker]
        if not (len(current_token) == 1 and "0" <= current_token <= "9"):
            index_tracker += 1
            continue
        else:
            parsed_number: int = int(current_token)
            numbers_collected.append(parsed_number)
            index_tracker += 1

    sum_numbers: int = 0
    position: int = 0
    while position < len(numbers_collected):
        sum_numbers += numbers_collected[position]
        position += 1

    result: int = total_number_of_fruits - sum_numbers
    return result