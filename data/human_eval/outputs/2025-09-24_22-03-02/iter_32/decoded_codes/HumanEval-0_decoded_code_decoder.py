from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    i = 0
    while i < len(numbers):
        elem = numbers[i]
        j = 0
        while j < len(numbers):
            elem2 = numbers[j]
            if i != j:
                difference = elem - elem2
                if difference < 0:
                    distance = -difference
                else:
                    distance = difference
                if distance < threshold:
                    return True
            j += 1
        i += 1
    return False