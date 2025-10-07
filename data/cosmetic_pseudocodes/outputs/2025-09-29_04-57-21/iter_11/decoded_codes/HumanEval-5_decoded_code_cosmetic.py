from typing import List

def intersperse(collection_of_ints: List[int], separator: int) -> List[int]:
    if not collection_of_ints:
        return []

    aggregated_collection: List[int] = []
    iterator_index: int = 0
    final_index: int = len(collection_of_ints) - 1

    while iterator_index < final_index:
        aggregated_collection.append(collection_of_ints[iterator_index])
        aggregated_collection.append(separator)
        iterator_index += 1

    aggregated_collection.append(collection_of_ints[final_index])

    return aggregated_collection