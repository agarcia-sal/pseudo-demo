from typing import List, Optional

def next_smallest(list_of_integers: List[int]) -> Optional[int]:
    filtered_numbers: List[int] = []
    for each_number in list_of_integers:
        if each_number not in filtered_numbers:
            filtered_numbers.append(each_number)
    filtered_numbers.sort()
    if len(filtered_numbers) < 2:
        return None
    return filtered_numbers[1]