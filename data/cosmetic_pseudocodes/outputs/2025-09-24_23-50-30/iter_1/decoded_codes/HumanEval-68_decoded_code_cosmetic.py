from typing import List, Union

def pluck(array_of_nodes: List[int]) -> List[Union[int, int]]:
    result_list: List[Union[int, int]] = []

    for element in array_of_nodes:
        if element % 2 != 0:
            continue
        if not result_list or element < result_list[0]:
            result_list = [element, array_of_nodes.index(element)]

    return result_list if result_list else []