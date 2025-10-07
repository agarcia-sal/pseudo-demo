from typing import List, Tuple

def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    coordinatesList: List[Tuple[int, int]] = []
    for mainIter in range(len(two_dimensional_list) - 1, -1, -1):
        row = two_dimensional_list[mainIter]
        for subIter in range(len(row)):
            currentValue = row[subIter]
            if currentValue == target_integer:
                coordinatesList.append((mainIter, subIter))
    # Sort by second element descending, then first element ascending
    coordinatesList.sort(key=lambda x: x[1], reverse=True)
    coordinatesList.sort(key=lambda x: x[0])
    return coordinatesList