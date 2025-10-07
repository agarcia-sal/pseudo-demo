from typing import List, Any

def common(list_one: List[Any], list_two: List[Any]) -> List[Any]:
    common_elements_set = set()
    for element_one in list_one:
        for element_two in list_two:
            if element_one == element_two:
                common_elements_set.add(element_one)
    common_elements_list = list(common_elements_set)
    common_elements_list.sort()
    return common_elements_list