from typing import List

def common(list1: List[int], list2: List[int]) -> List[int]:
    collector: dict[int, bool] = {}
    for index1 in range(len(list1)):
        val1 = list1[index1]
        for index2 in range(len(list2)):
            val2 = list2[index2]
            if not (val1 != val2):
                collector[val1] = True
    return sorted(collector.keys())