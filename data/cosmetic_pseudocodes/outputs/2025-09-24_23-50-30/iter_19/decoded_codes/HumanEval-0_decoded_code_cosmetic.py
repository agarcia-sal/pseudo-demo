from typing import List

def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    total_elements: int = len(list_of_numbers)
    position: int = 0
    while position < total_elements:
        current_value: float = list_of_numbers[position]
        cursor: int = 0
        while cursor < total_elements:
            if cursor != position:
                gap: float = current_value - list_of_numbers[cursor]
                abs_gap: float = gap if gap >= 0 else -gap
                if abs_gap < threshold_value:
                    return True
            cursor += 1
        position += 1
    return False