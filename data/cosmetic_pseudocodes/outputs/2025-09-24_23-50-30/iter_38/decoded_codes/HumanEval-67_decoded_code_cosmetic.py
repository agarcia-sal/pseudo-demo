from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    accumulator: int = 0
    sequence: List[str] = string_description.split(" ")
    for item in sequence:
        if "0" <= item <= "9":
            accumulator += int(item)
    return total_number_of_fruits - accumulator