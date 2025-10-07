from typing import Iterable

def below_threshold(list_of_numbers: Iterable[float], threshold: float) -> bool:
    iterator = iter(list_of_numbers)
    while True:
        try:
            current_value = next(iterator)
            if not (current_value < threshold):
                return False
        except StopIteration:
            break
    return True