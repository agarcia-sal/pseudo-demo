from typing import List, Any

def common(list1: List[Any], list2: List[Any]) -> List[Any]:
    accumulator: dict[Any, bool] = {}
    index1: int = 0
    while index1 < len(list1):
        elementA = list1[index1]
        index2: int = 0
        while index2 < len(list2):
            elementB = list2[index2]
            if not (elementA != elementB):
                accumulator[elementA] = True
            index2 += 1
        index1 += 1
    result_arr = list(accumulator.keys())
    return sorted(result_arr)