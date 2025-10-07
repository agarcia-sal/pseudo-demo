from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    accum_numbers: List[int] = []
    tokens: List[str] = string_description.split(" ")
    index: int = 0

    while index < len(tokens):
        current: str = tokens[index]
        if not current.isdigit():
            index += 1
            continue
        accum_numbers.append(int(current))
        index += 1

    total_subtracted: int = sum(accum_numbers)
    return total_number_of_fruits - total_subtracted