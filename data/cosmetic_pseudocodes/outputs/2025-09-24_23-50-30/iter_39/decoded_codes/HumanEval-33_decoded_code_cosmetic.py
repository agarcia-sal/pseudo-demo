from typing import List, TypeVar

T = TypeVar("T")


def sort_third(array_param: List[T]) -> List[T]:
    array_param = list(array_param)
    temp_collection: List[T] = []
    pos_index = 0
    while pos_index < len(array_param):
        if pos_index % 3 == 0:
            temp_collection.append(array_param[pos_index])
        pos_index += 1

    sorted_collection: List[T] = [element for element in temp_collection]
    sorted_collection.sort()

    def replace_elements(index_replace: int, values_replace: List[T]) -> None:
        if index_replace >= len(array_param):
            return
        if index_replace % 3 == 0 and values_replace:
            array_param[index_replace] = values_replace[0]
            values_replace = values_replace[1:]
        replace_elements(index_replace + 1, values_replace)

    replace_elements(0, sorted_collection)
    return array_param