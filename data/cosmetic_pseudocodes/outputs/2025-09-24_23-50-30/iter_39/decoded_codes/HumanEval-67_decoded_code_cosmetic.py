from typing import List

def fruit_distribution(input_string: str, count_fruits: int) -> int:
    accumulator: int = 0
    array_elements: List[str] = input_string.split(" ")
    index_outer: int = 0
    while index_outer < len(array_elements):
        current_piece: str = array_elements[index_outer]
        # accumulate integer values for numeric strings only
        if not (current_piece < "0" or current_piece > "9"):
            accumulator += int(current_piece)
        index_outer += 1
    return count_fruits - accumulator