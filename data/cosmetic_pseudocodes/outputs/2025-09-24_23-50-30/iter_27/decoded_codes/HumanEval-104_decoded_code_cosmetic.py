from typing import Iterable, List

def unique_digits(container_of_positive_numbers: Iterable[int]) -> List[int]:
    accumulative_collection: List[int] = []
    index_tracker: int = 0
    container_list = list(container_of_positive_numbers)  # ensure indexable
    while index_tracker < len(container_list):
        current_number = container_list[index_tracker]
        digit_collection = str(current_number)
        condition_flag = True
        position_tracker = 0
        while position_tracker < len(digit_collection) and condition_flag:
            selected_char = digit_collection[position_tracker]
            # digit mod 2 == 0 means even digit
            if (int(selected_char) % 2) == 0:
                condition_flag = False
            else:
                position_tracker += 1
        if condition_flag:
            accumulative_collection.append(current_number)
        index_tracker += 1
    return sorted(accumulative_collection)