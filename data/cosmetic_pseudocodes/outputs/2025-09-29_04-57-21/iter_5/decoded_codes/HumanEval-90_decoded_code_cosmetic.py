from typing import List, Optional

def next_smallest(list_of_integers: List[int]) -> Optional[int]:
    filtered_numbers: List[int] = []
    seen = set()
    for number in list_of_integers:
        if number not in seen:
            seen.add(number)
            filtered_numbers.append(number)
    filtered_numbers.sort()

    if len(filtered_numbers) < 2:
        return None
    return filtered_numbers[1]