from typing import List, Any

def common(list1: List[Any], list2: List[Any]) -> List[Any]:
    common_elements = {element1 for element1 in list1 if element1 in list2}
    return sorted(common_elements)