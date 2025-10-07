from typing import List

def sort_array(collection: List[int]) -> List[int]:
    length_of_collection: int = len(collection)
    if length_of_collection == 0:
        return []
    else:
        first_element: int = collection[0]
        last_element: int = collection[length_of_collection - 1]
        combined_sum: int = first_element + last_element
        remainder: int = combined_sum % 2
        is_descending: bool = remainder == 0
        sorted_collection: List[int] = sorted(collection, reverse=is_descending)
        return sorted_collection