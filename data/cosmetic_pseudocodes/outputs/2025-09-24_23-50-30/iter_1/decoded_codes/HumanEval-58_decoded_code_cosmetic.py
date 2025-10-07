from typing import List, Any

def common(list1: List[Any], list2: List[Any]) -> List[Any]:
    temp_map = {}
    output: List[Any] = []

    for idx in range(len(list1)):
        temp_map[list1[idx]] = True

    for idx in range(len(list2)):
        if list2[idx] in temp_map and list2[idx] not in output:
            output.append(list2[idx])

    output.sort()
    return output