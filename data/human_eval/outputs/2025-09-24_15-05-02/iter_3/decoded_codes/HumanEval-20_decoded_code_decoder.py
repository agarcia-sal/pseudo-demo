from typing import List, Tuple, Optional

def find_closest_elements(numbers: List[float]) -> Optional[Tuple[float, float]]:
    if len(numbers) < 2:
        return None  # Not enough elements to form a pair

    closest_pair = None
    distance = None

    for idx in range(len(numbers)):
        elem = numbers[idx]
        for idx2 in range(len(numbers)):
            if idx == idx2:
                continue
            elem2 = numbers[idx2]
            new_distance = abs(elem - elem2)
            if distance is None or new_distance < distance:
                distance = new_distance
                # Store the pair sorted so that smaller element is first
                closest_pair = tuple(sorted((elem, elem2)))

    return closest_pair