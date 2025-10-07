from typing import List, Any

def common(list_one: List[Any], list_two: List[Any]) -> List[Any]:
    result_set = set()
    for element_one in list_one:
        for element_two in list_two:
            if element_one == element_two:
                result_set.add(element_one)
    result_list = sorted(result_set)
    return result_list