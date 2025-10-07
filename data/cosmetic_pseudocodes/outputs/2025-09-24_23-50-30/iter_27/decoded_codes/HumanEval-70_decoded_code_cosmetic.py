from typing import List, TypeVar

T = TypeVar('T')


def strange_sort_list(input_collection: List[T]) -> List[T]:
    result_sequence: List[T] = []
    indicator: bool = False
    collection = input_collection[:]  # work on a copy to avoid modifying the original list

    while collection:
        if not indicator:
            element = collection[0]
            for item in collection:
                if element > item:
                    element = item
        else:
            element = collection[0]
            for item in collection:
                if element < item:
                    element = item

        result_sequence.append(element)
        # Remove first occurrence of element
        temp_index = 0
        while temp_index < len(collection):
            if collection[temp_index] == element:
                collection = collection[:temp_index] + collection[temp_index+1:]
                break
            temp_index += 1

        indicator = not indicator

    return result_sequence