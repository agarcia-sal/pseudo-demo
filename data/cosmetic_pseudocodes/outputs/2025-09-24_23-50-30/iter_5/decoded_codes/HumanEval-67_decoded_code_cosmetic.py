import re
from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    def extract_digits(parts: List[str], index: int, collected: List[int]) -> List[int]:
        if index >= len(parts):
            return collected
        token = parts[index]
        if re.fullmatch(r"\d+", token):
            return extract_digits(parts, index + 1, collected + [int(token)])
        return extract_digits(parts, index + 1, collected)

    tokens = string_description.split(" ")
    numbers_list = extract_digits(tokens, 0, [])
    total_accumulated = sum(numbers_list)
    return total_number_of_fruits - total_accumulated