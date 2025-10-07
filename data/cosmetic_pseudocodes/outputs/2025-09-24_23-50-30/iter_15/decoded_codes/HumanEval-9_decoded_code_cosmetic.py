from typing import List, Optional

def rolling_max(list_of_numbers: List[int]) -> List[int]:
    tracker_maximum: Optional[int] = None
    output_collection: List[int] = []
    iterator_index: int = 0

    while iterator_index < len(list_of_numbers):
        current_element: int = list_of_numbers[iterator_index]

        if tracker_maximum is not None:
            if current_element > tracker_maximum:
                tracker_maximum = current_element
        else:
            tracker_maximum = current_element

        output_collection.append(tracker_maximum)
        iterator_index += 1

    return output_collection