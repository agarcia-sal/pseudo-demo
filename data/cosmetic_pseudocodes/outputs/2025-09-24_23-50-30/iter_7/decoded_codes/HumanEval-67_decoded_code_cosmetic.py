from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    accumulator: int = 0
    tokens: List[str] = string_description.split()
    index: int = 0
    while index < len(tokens):
        current: str = tokens[index]
        if "0" <= current <= "9":
            # Accumulate numeric token values
            accumulator += int(current)
        index += 1
    return total_number_of_fruits - accumulator