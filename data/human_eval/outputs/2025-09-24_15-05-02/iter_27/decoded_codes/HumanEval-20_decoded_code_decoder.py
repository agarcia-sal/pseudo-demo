from typing import Optional, Tuple, Sequence


def find_closest_elements(numbers: Sequence[int]) -> Optional[Tuple[int, int]]:
    if not numbers or len(numbers) < 2:
        # Cannot find a pair if fewer than two elements
        return None

    closest_pair: Optional[Tuple[int, int]] = None
    distance: Optional[int] = None

    length: int = len(numbers)
    for idx in range(length):
        elem: int = numbers[idx]
        for idx2 in range(length):
            if idx != idx2:
                elem2: int = numbers[idx2]
                new_distance: int = abs(elem - elem2)
                if distance is None or new_distance < distance:
                    distance = new_distance
                    # Store as a sorted tuple (smaller first)
                    closest_pair = (elem, elem2) if elem <= elem2 else (elem2, elem)

    return closest_pair