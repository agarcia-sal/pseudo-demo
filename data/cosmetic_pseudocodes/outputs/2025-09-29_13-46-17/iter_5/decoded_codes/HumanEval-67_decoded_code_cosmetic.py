import re
from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    tokens: List[str] = string_description.split()

    def process_elements(indexE: int, numbersAcc: int) -> int:
        if indexE >= len(tokens):
            return total_number_of_fruits - numbersAcc
        current_token = tokens[indexE]
        updated_accumulator = numbersAcc + (int(current_token) if re.fullmatch(r"\d+", current_token) else 0)
        return process_elements(indexE + 1, updated_accumulator)

    return process_elements(0, 0)