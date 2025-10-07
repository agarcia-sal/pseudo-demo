from typing import Iterable, List


def unique_digits(collection_of_pos_ints: Iterable[int]) -> List[int]:
    filtered_items: List[int] = []
    index_counter: int = 0
    collection_list = list(collection_of_pos_ints)  # Allow indexing and consistent length

    while index_counter < len(collection_list):
        current_item = collection_list[index_counter]
        digit_set = {int(d) for d in str(current_item)}
        contains_even_digit = any(d % 2 == 0 for d in digit_set)

        if not contains_even_digit:
            filtered_items.append(current_item)
        index_counter += 1

    return sorted(filtered_items)