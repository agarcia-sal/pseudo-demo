from typing import List


def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    pos_x: int = 0
    length: int = len(list_of_numbers)
    while pos_x < length:
        val_x: float = list_of_numbers[pos_x]
        pos_y: int = 0
        while pos_y < length:
            if pos_x == pos_y:
                pass  # skip comparison with self
            else:
                val_y: float = list_of_numbers[pos_y]
                diff: float = abs(val_x - val_y)
                if diff < threshold_value:
                    return True
            pos_y += 1
        pos_x += 1
    return False