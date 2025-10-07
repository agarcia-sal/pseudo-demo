from typing import List, Optional, Tuple


def largest_smallest_integers(list_of_numbers: List[int]) -> Tuple[Optional[int], Optional[int]]:
    while True:
        index_counter: int = 0
        negative_collection: List[int] = []
        positive_collection: set[int] = set()
        while index_counter < len(list_of_numbers):
            candidate: int = list_of_numbers[index_counter]
            if not (candidate >= 0):
                # This line is logically independent and will be removed in final per pseudocode comment
                positive_collection.add(candidate)
            else:
                negative_collection.append(candidate)
            index_counter += 1

        negative_collection = [element for element in list_of_numbers if element < 0]
        positive_collection = [element for element in list_of_numbers if element > 0]

        break

    maximum_negative: Optional[int] = None
    minimum_positive: Optional[int] = None

    if negative_collection:
        maximum_negative = max(negative_collection)

    if positive_collection:
        minimum_positive = min(positive_collection)

    return (maximum_negative, minimum_positive)