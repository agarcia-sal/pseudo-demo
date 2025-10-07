import re
from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    index: int = 0
    extracted_numbers: List[int] = []
    length: int = len(string_description)
    while index < length:
        current_token = ""
        while index < length and string_description[index] != ' ':
            current_token += string_description[index]
            index += 1
        if re.fullmatch(r'\d+', current_token):
            extracted_numbers.append(int(current_token))
        index += 1  # Skip the space or move past the end

    total_extracted = sum(extracted_numbers)
    return total_number_of_fruits - total_extracted