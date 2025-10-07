from typing import TypeVar, List, Dict

T = TypeVar('T')


def unique(list_of_elements: List[T]) -> List[T]:
    result_map: Dict[T, bool] = {}
    result_list: List[T] = []
    for element in list_of_elements:
        if element not in result_map:
            result_map[element] = True
            result_list.append(element)

    sorted_list: List[T] = []

    def insert_in_order(item: T, index: int) -> None:
        if index == len(sorted_list):
            sorted_list.append(item)
            return
        if item <= sorted_list[index]:
            sorted_list.insert(index, item)
            return
        insert_in_order(item, index + 1)

    for value in result_list:
        insert_in_order(value, 0)

    return sorted_list