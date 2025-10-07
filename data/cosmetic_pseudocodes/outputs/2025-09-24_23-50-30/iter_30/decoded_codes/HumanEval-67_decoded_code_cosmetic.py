from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    accumulator: int = 0

    def helper(sequence: List[str], index: int) -> None:
        nonlocal accumulator
        if index == len(sequence):
            return
        if sequence[index].isdigit():
            accumulator += int(sequence[index])
        helper(sequence, index + 1)

    helper(string_description.split(" "), 0)
    return total_number_of_fruits - accumulator