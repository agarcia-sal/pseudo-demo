from typing import Sequence, TypeVar, List

T = TypeVar('T')

def sort_third(collection_param: Sequence[T]) -> List[T]:
    duplicate_collection: List[T] = list(collection_param)
    extracted_elements: List[T] = [duplicate_collection[pos] for pos in range(len(duplicate_collection)) if pos % 3 == 0]
    ordered_elements: List[T] = sorted(extracted_elements)
    insert_pos = 0
    for index_var in range(len(duplicate_collection)):
        if index_var % 3 == 0:
            duplicate_collection[index_var] = ordered_elements[insert_pos]
            insert_pos += 1
    return duplicate_collection