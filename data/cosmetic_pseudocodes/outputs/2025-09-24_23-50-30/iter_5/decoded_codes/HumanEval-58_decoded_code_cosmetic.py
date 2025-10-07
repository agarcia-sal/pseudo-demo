from typing import List, Any

def common(list1: List[Any], list2: List[Any]) -> List[Any]:
    temp_storage = set()
    for idx in range(1, len(list1) + 1):
        if list1[idx - 1] in list2:
            temp_storage.add(list1[idx - 1])
    return sorted(temp_storage)