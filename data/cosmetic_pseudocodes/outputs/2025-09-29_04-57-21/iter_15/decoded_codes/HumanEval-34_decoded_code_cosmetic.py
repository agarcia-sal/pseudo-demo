from typing import List, TypeVar

T = TypeVar('T', bound=object)

def unique(list_of_elements: List[T]) -> List[T]:
    distinct_collection: set[T] = set()
    outcome_list: List[T] = []
    counter: int = 0

    while counter < len(list_of_elements):
        distinct_collection.add(list_of_elements[counter])
        counter += 1

    for each_item in distinct_collection:
        outcome_list.append(each_item)

    return sorted(outcome_list)