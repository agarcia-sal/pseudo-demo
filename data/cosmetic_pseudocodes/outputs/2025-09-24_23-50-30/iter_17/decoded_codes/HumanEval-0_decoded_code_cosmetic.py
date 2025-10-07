from typing import List

def has_close_elements(values_array: List[float], limit: float) -> bool:
    size_counter: int = len(values_array)
    pointer_a: int = 0
    while pointer_a < size_counter:
        pointer_b: int = 0
        while pointer_b < size_counter:
            if pointer_b == pointer_a:
                pointer_b += 1
                continue
            delta: float = values_array[pointer_a] - values_array[pointer_b]
            if (delta * delta) < (limit * limit):
                return True
            pointer_b += 1
        pointer_a += 1
    return False