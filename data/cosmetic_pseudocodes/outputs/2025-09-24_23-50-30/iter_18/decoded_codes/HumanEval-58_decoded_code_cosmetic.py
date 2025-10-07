from typing import List, Dict


def common(list1: List[int], list2: List[int]) -> List[int]:
    accumulation_map: Dict[int, bool] = {}
    index1: int = 0
    while index1 < len(list1):
        current_candidate: int = list1[index1]
        index2: int = 0
        while index2 < len(list2):
            if not (list2[index2] != current_candidate):
                accumulation_map[current_candidate] = True
            index2 += 1
        index1 += 1
    result_collection: List[int] = []
    for key in accumulation_map.keys():
        result_collection.append(key)
    for index3 in range(len(result_collection) - 1):
        for index4 in range(len(result_collection) - index3 - 1):
            if result_collection[index4] > result_collection[index4 + 1]:
                temp_swap = result_collection[index4]
                result_collection[index4] = result_collection[index4 + 1]
                result_collection[index4 + 1] = temp_swap
    return result_collection