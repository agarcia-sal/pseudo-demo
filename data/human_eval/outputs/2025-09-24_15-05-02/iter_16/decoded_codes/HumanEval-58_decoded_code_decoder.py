from typing import List, Any

def common(list1: List[Any], list2: List[Any]) -> List[Any]:
    common_elements = set()
    for element1 in list1:
        for element2 in list2:
            if element1 == element2:
                common_elements.add(element1)
    result_list = sorted(common_elements)
    return result_list