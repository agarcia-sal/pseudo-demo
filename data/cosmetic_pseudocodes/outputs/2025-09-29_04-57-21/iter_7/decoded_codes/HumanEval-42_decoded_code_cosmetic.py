from typing import Iterable, List

def incr_list(collection_of_items: Iterable[int]) -> List[int]:
    resultant_list: List[int] = []
    index: int = 0
    # Iterate using index until index reaches length of the collection
    items = list(collection_of_items)  # Ensure index access
    length = len(items)
    while index < length:
        item = items[index]
        incremented_value = item + 1
        resultant_list.append(incremented_value)
        index += 1
    return resultant_list